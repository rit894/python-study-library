DEBUG = False
TRACE = False

# ---------------------------
# File paths (basic text I/O)
# ---------------------------

BOOKS_FILE = "books.txt"
MEMBERS_FILE = "members.txt"
LOANS_FILE = "loans.txt"
BOOKINGS_FILE = "bookings.txt"

# ---------------------------
# Helper: printing for debug/trace
# ---------------------------

def debug(msg):
    if DEBUG:
        print("[DEBUG]", msg)

def trace(msg):
    if TRACE:
        print("[TRACE]", msg)

# ---------------------------
# Helper: safe int conversion
# ---------------------------

def to_int(s, default=0):
    try:
        return int(s)
    except:
        return default

# ---------------------------
# Helper: simple date/time
# ---------------------------

def today_date():
    # Simple YYYY-MM-DD using local system via splitting (no imports)
    # In real projects, you'd use datetime, but we avoid imports per syllabus constraint.
    # We'll ask user to enter dates where needed and store them as strings.
    return "TODAY"

def now_time():
    # Simple placeholder; demonstration only
    return "NOW"

# ---------------------------
# Validation helpers (logical reasoning)
# ---------------------------

def non_empty(s):
    return s is not None and str(s).strip() != ""

def valid_email(s):
    s = s.strip()
    return ("@" in s) and ("." in s) and len(s) >= 5

def valid_phone(s):
    digits = "".join([c for c in s if c.isdigit()])
    return len(digits) >= 7 and len(digits) <= 14

# ---------------------------
# Persistence: generic read/write for pipe-delimited records
# ---------------------------

def read_lines(path):
    try:
        with open(path, "r") as f:
            return [line.rstrip("\n") for line in f]
    except:
        return []

def write_lines(path, lines):
    with open(path, "w") as f:
        for line in lines:
            f.write(line + "\n")

# ---------------------------
# ID generation (incremental)
# ---------------------------

def gen_id(prefix, existing_ids):
    # Incremental numeric suffix, zero-padded to 4 digits for readability
    i = 1
    while True:
        candidate = prefix + str(i).zfill(4)
        if candidate not in existing_ids:
            debug("Generated ID: " + candidate)
            return candidate
        i += 1

# ---------------------------
# Books: load/save and operations
# ---------------------------

def parse_book_line(line):
    # id|title|author|category|tags(; separated)|copies_total|copies_available|added_on
    parts = line.split("|")
    if len(parts) != 8:
        return None
    tags_list = [t.strip().lower() for t in parts[4].split(";") if t.strip() != ""]
    return {
        "id": parts[0],
        "title": parts[1],
        "author": parts[2],
        "category": parts[3],
        "tags": tags_list,
        "copies_total": to_int(parts[5], 0),
        "copies_available": to_int(parts[6], 0),
        "added_on": parts[7]
    }

def book_to_line(book):
    tags_str = ";".join(book.get("tags", []))
    return "|".join([
        book["id"],
        book["title"],
        book["author"],
        book["category"],
        tags_str,
        str(book["copies_total"]),
        str(book["copies_available"]),
        book["added_on"]
    ])

def load_books():
    lines = read_lines(BOOKS_FILE)
    books = []
    for line in lines:
        b = parse_book_line(line)
        if b is not None:
            books.append(b)
    return books

def save_books(books):
    lines = []
    for b in books:
        lines.append(book_to_line(b))
    write_lines(BOOKS_FILE, lines)

def add_book():
    books = load_books()
    existing_ids = set([b["id"] for b in books])
    book_id = gen_id("B", existing_ids)

    print("\nAdd a new book")
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()
    category = input("Enter category path (e.g., Technology/Programming/Python): ").strip()
    tags = input("Enter tags (semicolon-separated, e.g., python;algorithm;sorting): ").strip()
    copies_total_str = input("Enter total copies (integer): ").strip()

    if not (non_empty(title) and non_empty(author) and non_empty(category)):
        print("Invalid: Title/Author/Category cannot be empty.")
        return

    copies_total = to_int(copies_total_str, -1)
    if copies_total <= 0:
        print("Invalid: copies must be a positive integer.")
        return

    tag_list = [t.strip().lower() for t in tags.split(";") if t.strip() != ""]
    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "category": category,
        "tags": tag_list,
        "copies_total": copies_total,
        "copies_available": copies_total,
        "added_on": today_date()
    }
    books.append(new_book)
    save_books(books)
    print("Book added:", book_id, "-", title)

def list_books():
    books = load_books()
    if len(books) == 0:
        print("No books found.")
        return
    print("\nTotal books:", len(books))
    for b in books:
        print(b["id"], "|", b["title"], "|", b["author"], "|", b["category"], "| Avail:", str(b["copies_available"]) + "/" + str(b["copies_total"]))

def update_book():
    books = load_books()
    book_id = input("Enter book ID to update: ").strip()
    target = None
    for b in books:
        if b["id"] == book_id:
            target = b
            break
    if target is None:
        print("Book not found.")
        return

    print("Updating", target["id"], "-", target["title"])
    new_title = input("New title (blank to keep): ").strip()
    new_author = input("New author (blank to keep): ").strip()
    new_category = input("New category (blank to keep): ").strip()
    new_tags = input("New tags (semicolon-separated, blank to keep): ").strip()
    new_total = input("New total copies (blank to keep): ").strip()

    if non_empty(new_title): target["title"] = new_title
    if non_empty(new_author): target["author"] = new_author
    if non_empty(new_category): target["category"] = new_category
    if non_empty(new_tags):
        target["tags"] = [t.strip().lower() for t in new_tags.split(";") if t.strip() != ""]
    if non_empty(new_total):
        nt = to_int(new_total, -1)
        if nt > 0 and nt >= target["copies_total"]:
            # Adjust available by difference to avoid negative logic for simplicity
            diff = nt - target["copies_total"]
            target["copies_total"] = nt
            target["copies_available"] += diff
        else:
            print("Invalid total copies; must be >= current total.")

    save_books(books)
    print("Book updated.")

def remove_book():
    books = load_books()
    book_id = input("Enter book ID to remove: ").strip()
    # Check active loans for this book
    loans = load_loans()
    for l in loans:
        if l["book_id"] == book_id and l["returned_on"] == "":
            print("Cannot remove: book has active loans.")
            return
    new_books = []
    removed = False
    for b in books:
        if b["id"] == book_id:
            removed = True
        else:
            new_books.append(b)
    if removed:
        save_books(new_books)
        print("Book removed.")
    else:
        print("Book not found.")

# ---------------------------
# Members: load/save and operations
# ---------------------------

def parse_member_line(line):
    # id|name|email|phone|joined_on|active
    parts = line.split("|")
    if len(parts) != 6:
        return None
    active_val = True if parts[5].strip().lower() == "true" else False
    return {
        "id": parts[0],
        "name": parts[1],
        "email": parts[2],
        "phone": parts[3],
        "joined_on": parts[4],
        "active": active_val
    }

def member_to_line(m):
    active_str = "true" if m.get("active", True) else "false"
    return "|".join([m["id"], m["name"], m["email"], m["phone"], m["joined_on"], active_str])

def load_members():
    lines = read_lines(MEMBERS_FILE)
    members = []
    for line in lines:
        m = parse_member_line(line)
        if m is not None:
            members.append(m)
    return members

def save_members(members):
    lines = []
    for m in members:
        lines.append(member_to_line(m))
    write_lines(MEMBERS_FILE, lines)

def add_member():
    members = load_members()
    existing_ids = set([m["id"] for m in members])
    member_id = gen_id("M", existing_ids)

    print("\nAdd a new member")
    name = input("Enter full name: ").strip()
    email = input("Enter email: ").strip()
    phone = input("Enter phone: ").strip()

    if not non_empty(name):
        print("Invalid name.")
        return
    if not valid_email(email):
        print("Invalid email.")
        return
    if not valid_phone(phone):
        print("Invalid phone.")
        return

    new_member = {
        "id": member_id,
        "name": name,
        "email": email,
        "phone": phone,
        "joined_on": today_date(),
        "active": True
    }
    members.append(new_member)
    save_members(members)
    print("Member added:", member_id, "-", name)

def list_members():
    members = load_members()
    if len(members) == 0:
        print("No members found.")
        return
    print("\nTotal members:", len(members))
    for m in members:
        status = "Active" if m["active"] else "Inactive"
        print(m["id"], "|", m["name"], "|", m["email"], "|", m["phone"], "|", status)

def update_member():
    members = load_members()
    member_id = input("Enter member ID to update: ").strip()
    target = None
    for m in members:
        if m["id"] == member_id:
            target = m
            break
    if target is None:
        print("Member not found.")
        return

    print("Updating", target["id"], "-", target["name"])
    new_name = input("New name (blank to keep): ").strip()
    new_email = input("New email (blank to keep): ").strip()
    new_phone = input("New phone (blank to keep): ").strip()
    toggle_active = input("Toggle active status? (y/n): ").strip().lower()

    if non_empty(new_name): target["name"] = new_name
    if non_empty(new_email) and valid_email(new_email): target["email"] = new_email
    if non_empty(new_phone) and valid_phone(new_phone): target["phone"] = new_phone
    if toggle_active == "y":
        target["active"] = not target["active"]

    save_members(members)
    print("Member updated.")

def remove_member():
    members = load_members()
    member_id = input("Enter member ID to remove: ").strip()
    # Prevent removal if active loans exist
    loans = load_loans()
    for l in loans:
        if l["member_id"] == member_id and l["returned_on"] == "":
            print("Cannot remove: member has active loans.")
            return
    new_members = []
    removed = False
    for m in members:
        if m["id"] == member_id:
            removed = True
        else:
            new_members.append(m)
    if removed:
        save_members(new_members)
        print("Member removed.")
    else:
        print("Member not found.")

# ---------------------------
# Loans: load/save and operations
# ---------------------------

def parse_loan_line(line):
    # loan_id|book_id|member_id|loan_date|due_date|returned_on
    parts = line.split("|")
    if len(parts) != 6:
        return None
    returned_on = parts[5].strip()
    return {
        "loan_id": parts[0],
        "book_id": parts[1],
        "member_id": parts[2],
        "loan_date": parts[3],
        "due_date": parts[4],
        "returned_on": returned_on  # "" means not returned
    }

def loan_to_line(l):
    return "|".join([l["loan_id"], l["book_id"], l["member_id"], l["loan_date"], l["due_date"], l["returned_on"]])

def load_loans():
    lines = read_lines(LOANS_FILE)
    loans = []
    for line in lines:
        l = parse_loan_line(line)
        if l is not None:
            loans.append(l)
    return loans

def save_loans(loans):
    lines = []
    for l in loans:
        lines.append(loan_to_line(l))
    write_lines(LOANS_FILE, lines)

def issue_loan():
    books = load_books()
    members = load_members()
    loans = load_loans()

    book_id = input("Enter book ID to loan: ").strip()
    member_id = input("Enter member ID: ").strip()

    book = None
    for b in books:
        if b["id"] == book_id:
            book = b
            break
    member = None
    for m in members:
        if m["id"] == member_id:
            member = m
            break

    if book is None:
        print("Book not found.")
        return
    if member is None:
        print("Member not found.")
        return
    if not member["active"]:
        print("Member inactive; cannot issue loan.")
        return
    if book["copies_available"] <= 0:
        print("No copies available.")
        return

    existing_ids = set([l["loan_id"] for l in loans])
    loan_id = gen_id("L", existing_ids)
    loan_date = today_date()
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()  # kept as string for simplicity

    new_loan = {
        "loan_id": loan_id,
        "book_id": book_id,
        "member_id": member_id,
        "loan_date": loan_date,
        "due_date": due_date,
        "returned_on": ""
    }
    loans.append(new_loan)
    book["copies_available"] -= 1

    save_loans(loans)
    save_books(books)
    print("Loan issued:", loan_id, "| Due:", due_date)

def return_loan():
    loans = load_loans()
    books = load_books()
    loan_id = input("Enter loan ID to return: ").strip()

    target = None
    for l in loans:
        if l["loan_id"] == loan_id:
            target = l
            break
    if target is None:
        print("Loan not found.")
        return
    if target["returned_on"] != "":
        print("Loan already returned.")
        return

    target["returned_on"] = today_date()
    # restore availability
    book = None
    for b in books:
        if b["id"] == target["book_id"]:
            book = b
            break
    if book is not None:
        book["copies_available"] += 1

    save_loans(loans)
    save_books(books)
    print("Return processed.")

def list_loans():
    loans = load_loans()
    if len(loans) == 0:
        print("No loans found.")
        return
    print("\nTotal loans:", len(loans))
    for l in loans:
        status = "Returned" if l["returned_on"] != "" else "Active"
        print(l["loan_id"], "| Book:", l["book_id"], "| Member:", l["member_id"], "| Due:", l["due_date"], "| Status:", status)

# ---------------------------
# Study room bookings: load/save and operations
# ---------------------------

def parse_booking_line(line):
    # booking_id|member_id|room|start_time|end_time|purpose
    parts = line.split("|")
    if len(parts) != 6:
        return None
    return {
        "booking_id": parts[0],
        "member_id": parts[1],
        "room": parts[2],
        "start_time": parts[3],
        "end_time": parts[4],
        "purpose": parts[5]
    }

def booking_to_line(b):
    return "|".join([b["booking_id"], b["member_id"], b["room"], b["start_time"], b["end_time"], b["purpose"]])

def load_bookings():
    lines = read_lines(BOOKINGS_FILE)
    bookings = []
    for line in lines:
        b = parse_booking_line(line)
        if b is not None:
            bookings.append(b)
    return bookings

def save_bookings(bookings):
    lines = []
    for b in bookings:
        lines.append(booking_to_line(b))
    write_lines(BOOKINGS_FILE, lines)

def book_study_room():
    members = load_members()
    bookings = load_bookings()

    member_id = input("Enter member ID: ").strip()
    # Ensure member exists and is active
    member = None
    for m in members:
        if m["id"] == member_id:
            member = m
            break
    if member is None or not member["active"]:
        print("Member not found or inactive.")
        return

    room = input("Enter room name (e.g., Room-101): ").strip()
    start = input("Enter start time (YYYY-MM-DD HH:MM): ").strip()
    end = input("Enter end time (YYYY-MM-DD HH:MM): ").strip()
    purpose = input("Enter purpose (e.g., Group study): ").strip()

    existing_ids = set([b["booking_id"] for b in bookings])
    booking_id = gen_id("S", existing_ids)

    # Simple conflict check: if same room and overlapping string ranges
    # We'll compare lexicographically (assuming same format); this is illustrative.
    for b in bookings:
        if b["room"] == room:
            s1 = b["start_time"]
            e1 = b["end_time"]
            s2 = start
            e2 = end
            # overlap if not (end <= start1 or start >= end1)
            if not (e2 <= s1 or s2 >= e1):
                print("Time conflict detected with existing booking:", b["booking_id"])
                return

    new_booking = {
        "booking_id": booking_id,
        "member_id": member_id,
        "room": room,
        "start_time": start,
        "end_time": end,
        "purpose": purpose
    }
    bookings.append(new_booking)
    save_bookings(bookings)
    print("Booking confirmed:", booking_id)

def list_bookings():
    bookings = load_bookings()
    if len(bookings) == 0:
        print("No bookings found.")
        return
    print("\nTotal bookings:", len(bookings))
    for b in bookings:
        print(b["booking_id"], "| Member:", b["member_id"], "|", b["room"], "|", b["start_time"], "->", b["end_time"], "|", b["purpose"])

# ---------------------------
# Algorithms: Searching (linear, binary)
# ---------------------------

def linear_search_books_by_title(books, query):
    q = query.strip().lower()
    result = []
    for b in books:
        if q in b["title"].lower():
            result.append(b)
    trace("linear_search found " + str(len(result)) + " matches for '" + q + "'")
    return result

def binary_search_sorted_strings(arr, target):
    # arr must be sorted ascending
    lo = 0
    hi = len(arr) - 1
    t = target.lower()
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_val = arr[mid].lower()
        trace("binary_search lo=" + str(lo) + " hi=" + str(hi) + " mid=" + str(mid) + " val=" + mid_val)
        if mid_val == t:
            return mid
        elif mid_val < t:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# ---------------------------
# Algorithms: Sorting (bubble, insertion, selection, merge, quicksort)
# ---------------------------

def bubble_sort_books_by_title(books):
    arr = books[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j]["title"].lower() > arr[j + 1]["title"].lower():
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        trace("bubble_sort pass " + str(i) + " swapped=" + str(swapped))
        if not swapped:
            break
    return arr

def insertion_sort_members_by_name(members):
    arr = members[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j]["name"].lower() > key["name"].lower():
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        trace("insertion_sort inserted " + key["name"])
    return arr

def selection_sort_books_by_author(books):
    arr = books[:]
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j]["author"].lower() < arr[min_idx]["author"].lower():
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        trace("selection_sort i=" + str(i) + " min_idx=" + str(min_idx))
    return arr

def merge_sort_books_by_availability(books):
    arr = books[:]
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_books_by_availability(arr[:mid])
    right = merge_sort_books_by_availability(arr[mid:])
    merged = merge_books_by_availability(left, right)
    trace("merge_sort split len=" + str(len(arr)) + " mid=" + str(mid))
    return merged

def merge_books_by_availability(left, right):
    result = []
    i = 0
    j = 0
    # Descending by copies_available
    while i < len(left) and j < len(right):
        if left[i]["copies_available"] >= right[j]["copies_available"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def quicksort_loans_by_due(loans):
    # Recursion-based quicksort (ascending by due_date string)
    if len(loans) <= 1:
        return loans[:]
    pivot = loans[len(loans) // 2]["due_date"]
    left = []
    middle = []
    right = []
    for x in loans:
        if x["due_date"] < pivot:
            left.append(x)
        elif x["due_date"] == pivot:
            middle.append(x)
        else:
            right.append(x)
    trace("quicksort pivot=" + pivot + " left=" + str(len(left)) + " mid=" + str(len(middle)) + " right=" + str(len(right)))
    return quicksort_loans_by_due(left) + middle + quicksort_loans_by_due(right)

# ---------------------------
# Recursion demo: category traversal
# ---------------------------

def traverse_category_path(category):
    # Given "Technology/Programming/Python"
    # Return ["Technology", "Technology/Programming", "Technology/Programming/Python"]
    parts = [p for p in category.split("/") if p.strip() != ""]
    result = []
    def helper(idx):
        if idx >= len(parts):
            return
        current = "/".join(parts[:idx + 1])
        result.append(current)
        trace("traverse idx=" + str(idx) + " current=" + current)
        helper(idx + 1)
    helper(0)
    return result

# ---------------------------
# Analytics: tag frequency and availability ranking
# ---------------------------

def top_k_tags(books, k):
    freq = {}
    for b in books:
        for t in b.get("tags", []):
            freq[t] = freq.get(t, 0) + 1
    items = []
    for key in freq:
        items.append((key, freq[key]))
    # sort by frequency desc, then tag asc
    items.sort(key=lambda x: (-x[1], x[0]))
    return items[:k]

# ---------------------------
# Workflows: search and sort (user-facing)
# ---------------------------

def search_books_flow():
    books = load_books()
    if len(books) == 0:
        print("No books available to search.")
        return
    query = input("Enter title query for linear search: ").strip()
    matches = linear_search_books_by_title(books, query)
    if len(matches) == 0:
        print("No matches found (linear search).")
    else:
        print("Linear search matches:", len(matches))
        for b in matches:
            print(b["id"], "|", b["title"], "|", b["author"])

    titles = []
    # unique titles
    seen = set()
    for b in books:
        if b["title"] not in seen:
            titles.append(b["title"])
            seen.add(b["title"])
    titles.sort()
    exact = input("Enter exact title for binary search (case-insensitive): ").strip()
    idx = binary_search_sorted_strings(titles, exact)
    if idx >= 0:
        print("Binary search: title found at index", idx, "in sorted titles.")
    else:
        print("Binary search: exact title not found.")

def sort_books_flow():
    books = load_books()
    if len(books) == 0:
        print("No books available to sort.")
        return
    print("\nSort options:")
    print("1. Bubble sort by title (asc)")
    print("2. Selection sort by author (asc)")
    print("3. Merge sort by availability (desc)")
    choice = input("Choose option (1-3): ").strip()
    if choice == "1":
        sorted_books = bubble_sort_books_by_title(books)
    elif choice == "2":
        sorted_books = selection_sort_books_by_author(books)
    elif choice == "3":
        sorted_books = merge_sort_books_by_availability(books)
    else:
        print("Invalid choice.")
        return
    for b in sorted_books:
        print(b["id"], "|", b["title"], "|", b["author"], "| Avail:", b["copies_available"])

def sort_members_flow():
    members = load_members()
    if len(members) == 0:
        print("No members available to sort.")
        return
    sorted_members = insertion_sort_members_by_name(members)
    for m in sorted_members:
        status = "Active" if m["active"] else "Inactive"
        print(m["id"], "|", m["name"], "|", status)

def sort_loans_flow():
    loans = load_loans()
    if len(loans) == 0:
        print("No loans available to sort.")
        return
    sorted_loans = quicksort_loans_by_due(loans)
    for l in sorted_loans:
        print(l["loan_id"], "| Book:", l["book_id"], "| Member:", l["member_id"], "| Due:", l["due_date"], "| Returned:", l["returned_on"])

def category_explore_flow():
    books = load_books()
    if len(books) == 0:
        print("No books available.")
        return
    book_id = input("Enter book ID for category exploration: ").strip()
    book = None
    for b in books:
        if b["id"] == book_id:
            book = b
            break
    if book is None:
        print("Book not found.")
        return
    paths = traverse_category_path(book["category"])
    print("Category hierarchy:")
    for p in paths:
        print("-", p)

# ---------------------------
# Settings: Toggle debug/trace
# ---------------------------

def toggle_debug_trace():
    global DEBUG, TRACE
    print("Current DEBUG=", DEBUG, "TRACE=", TRACE)
    d = input("Toggle DEBUG? (y/n): ").strip().lower()
    t = input("Toggle TRACE? (y/n): ").strip().lower()
    if d == "y":
        DEBUG = not DEBUG
    if t == "y":
        TRACE = not TRACE
    print("Updated DEBUG=", DEBUG, "TRACE=", TRACE)

# ---------------------------
# Menus: Books
# ---------------------------

def books_menu():
    while True:
        print("\n[Books Menu]")
        print("1. Add book")
        print("2. List books")
        print("3. Update book")
        print("4. Remove book")
        print("5. Search books (linear + binary)")
        print("6. Sort books (bubble/selection/merge)")
        print("7. Explore category hierarchy (recursion)")
        print("0. Back")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_book()
        elif choice == "2":
            list_books()
        elif choice == "3":
            update_book()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            search_books_flow()
        elif choice == "6":
            sort_books_flow()
        elif choice == "7":
            category_explore_flow()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

# ---------------------------
# Menus: Members
# ---------------------------

def members_menu():
    while True:
        print("\n[Members Menu]")
        print("1. Add member")
        print("2. List members")
        print("3. Update member")
        print("4. Remove member")
        print("5. Sort members by name (Insertion sort)")
        print("0. Back")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_member()
        elif choice == "2":
            list_members()
        elif choice == "3":
            update_member()
        elif choice == "4":
            remove_member()
        elif choice == "5":
            sort_members_flow()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

# ---------------------------
# Menus: Loans
# ---------------------------

def loans_menu():
    while True:
        print("\n[Loans Menu]")
        print("1. Issue loan")
        print("2. Return loan")
        print("3. List loans")
        print("4. Sort loans by due date (Quicksort)")
        print("0. Back")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            issue_loan()
        elif choice == "2":
            return_loan()
        elif choice == "3":
            list_loans()
        elif choice == "4":
            sort_loans_flow()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

# ---------------------------
# Menus: Study rooms
# ---------------------------

def study_menu():
    while True:
        print("\n[Study Rooms Menu]")
        print("1. Book a study room")
        print("2. List bookings")
        print("0. Back")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            book_study_room()
        elif choice == "2":
            list_bookings()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

# ---------------------------
# Menus: Analytics
# ---------------------------

def analytics_menu():
    while True:
        print("\n[Analytics Menu]")
        print("1. Top-5 tags among books")
        print("2. Availability ranking (Merge sort)")
        print("0. Back")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            books = load_books()
            tags = top_k_tags(books, 5)
            print("Top tags:")
            for item in tags:
                print("-", item[0], ":", item[1])
        elif choice == "2":
            books = load_books()
            sorted_books = merge_sort_books_by_availability(books)
            print("Books ranked by availability (desc):")
            for b in sorted_books:
                print(b["id"], "|", b["title"], "| Avail:", b["copies_available"])
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

# ---------------------------
# Menu: Settings
# ---------------------------

def settings_menu():
    while True:
        print("\n[Settings]")
        print("1. Toggle debug/trace")
        print("0. Back")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            toggle_debug_trace()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

# ---------------------------
# Main menu (Program orchestration)
# ---------------------------

def main_menu():
    print("Welcome to the Community Library & Study Hub Manager")
    print("Session started at", now_time())
    while True:
        print("\n[Main Menu]")
        print("1. Books")
        print("2. Members")
        print("3. Loans")
        print("4. Study Rooms")
        print("5. Analytics")
        print("6. Settings")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            books_menu()
        elif choice == "2":
            members_menu()
        elif choice == "3":
            loans_menu()
        elif choice == "4":
            study_menu()
        elif choice == "5":
            analytics_menu()
        elif choice == "6":
            settings_menu()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# ---------------------------
# Entry point
# ---------------------------

if __name__ == "__main__":
    main_menu()
