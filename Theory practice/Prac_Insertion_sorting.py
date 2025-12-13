def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        insert_pos = i  

        for j in range(i - 1, -1, -1):
            if arr[j] > key:
                arr[j + 1] = arr[j]  
                insert_pos = j       
            else:
                break

        arr[insert_pos] = key  
# for and while loop combination 
def Insertion_sort(arr):
    # Outer loop with FOR → picks each element
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Inner loop with WHILE → shifts elements
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]   # shift element right
            j -= 1

        # Place the key at its correct position
        arr[j + 1] = key

# Example usage
data = [8, 3, 5, 4, 6, 1]
print("Original:", data)
Insertion_sort(data)
print("Sorted:", data)


#  Pure recursive format of the insertion sorting
def insertion_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    if n <= 1:
        return

    # Sort first n-1 elements
    insertion_sort_recursive(arr, n-1)

    # Insert nth element
    key = arr[n-1]
    j = n-2
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key

# Insertion sorting using only while loops 
def insertion_sort(arr):
    i = 1   # start from index 1
    while i < len(arr):   # outer loop
        key = arr[i]
        j = i - 1

        # inner loop for shifting
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        i += 1   # move to next element

# Example usage
data = [8, 3, 5, 4, 6, 1]
print("Original:", data)
insertion_sort(data)
print("Sorted:", data)




