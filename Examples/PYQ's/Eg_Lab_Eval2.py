# '''1.	A store keeps a list of product dictionaries:'''
# products = [
#     {"id": 101, "name": "Laptop", "price": 900, "stock": 12},
#     {"id": 205, "name": "Keyboard", "price": 25, "stock": 85},
#     {"id": 150, "name": "Monitor", "price": 180, "stock": 30},
    
# ]

# # Write a python program to:
# # a)	Sort the products:
# # i.	by price (low → high)
# # ii.	by stock (high → low)
# # iii.	alphabetically by name
# # b)	Search for a product:
# # i.	by product ID (binary search)
# # ii.	by name (linear search / partial match)
# # iii.Add a function that returns all products with price within a user-defined range.
# price=[]
# for char in products:
#         x= (char['name'])
#         price.append(x)
#         print(price)
          
# for i in range(len(price)):
#         for j in range(0,len(price)-1-i):
#                 if price[j]>price[j+1]:
#                         price[j],price[j+1]=price[j+1],price[j]
# print(price)
# high=len(price)-1
# low=0
# target='Monitor'
# while low<=high:
#         mid=(high+low)//2
#         if price[mid]==target:
#                 print(f'target found at {mid} index')
#                 break
#         elif price[mid]< target:
#                 low = mid+1
#         elif price[mid]>target:
#                 high=mid-1
# N=int(input())

# students=[]
# for i in range(N):
#     roll_number=int(input())
#     marks=int(input())
#     students.append([roll_number,marks])
# for i in range(len(students)):
#     for j in range(0,len(students)-1-i):
#         if students[j][1]<students[j+1][1]:
#            students[j], students[j+1]=students[j+1],students[j]
# print(students)
# high=len(students)-1
# low=0
# target=int(input())
# found = False
# while low<=high:
#     mid=(low+high)//2
#     if students[mid][0]==target:
#         print(f"rank:{mid+1}, marks:{students[mid][1]}")
#         found = True
#         break
#     elif students[mid][0]<target:
#         low=mid+1
#     elif students[mid][0]>target:
#         high =mid-1
# if not found:
#         print("not found")
'''.Library System-Search by Book Title
A college library wants to quickly check whether a particular book title is
available.
• Read N, the number of books.
• For each book, read the title (string) and author name (string).
Assume all titles are unique.
• Store all books in a suitable structure.
• First, sort the books in ascending alphabetical order of title
using selection sort.
• Then read a book title to be searched.
• Apply binary search on the sorted list (by title) to check whether
the title exists.
• If found, print the full details of the book (title and author). If not
found, print “Book not available”.
You must write your own sorting and binary search functions; built-in
sorting and searching are not allowed.'''
'''N=int(input())
list1=[]
for i in range(N):
    book= input()
    author=input()
    list1.append([book,author])
for i in range(len(list1)):
    min_index=i
    for j in range(i+1,len(list1)):
        if list1[j][0]<list1[min_index][0]:
         min_index=j
    list1[i],list1[min_index]= list1[min_index],list1[i]
    print(list1)
high=len(list1)-1
low=0
target = input()
found = False
while low<=high:
    mid=(low+high)//2
    if list1[mid][0]==target:
        
        print(f"Title: {list1[mid][0]}, Author: {list1[mid][1]}")
        found = True
        break

    elif list1[mid][0]<target:
        low=mid+1
    elif list1[mid][0]>target:
        high =mid-1
if not found:
        print("not found")'''
'''n= int(input())
list1=[]
for i in range(n):
    number=int(input()) 
    name=input()
    list1.append([name,number])
print(list1)
for i in range(len(list1)):
    min_index=i
    for j in range(i+1,len(list1)):
        if list1[j][0]<list1[min_index][0]:
            min_index=j
    list1[i],list1[min_index]=list1[min_index],list1[i]
high=len(list1)-1
low=0
target=int(input())
found= False
while low<=high:
    mid=(high+low)//2
    if list1[mid]==target:
        print(list1[mid][1])
        found=True
    elif list1[mid]<target:
        low=mid+1
    elif list1[mid]>target:
        high=mid-1
if not found:
    print('not found')
    # bubble sortd
for i in range(len(list1)):
    for j in range(0,len(list1)-1-i):
        if list1[j][1]<list1[j+1][1]:
            list1[j],list1[j+1]=list1[j+1],list1[j] 
            # Selection sort 
for i in range(len(list1)):
    min_index=i
    for j in range(i+1,len(list1)):
        if list1[j]>list1[min_index]:
            min_index=j
        list1[i],list1[min_index]=list1[min_index],list1[i]
n= int(input())
list1=[]
for i in range(n):
    N=float(input())
    list1.append(N)
for i in range(1,len(list1)):
    key= list1[i]
    ip=i
    for j in range(i-1,-1,-1):
        if list1[j]>key:
            list1[j+1]=list1[j]
            ip=j
        else:
            break
target= float(input())
low,high= 0,len(list1)-1
while low<=high:
    mid=(high+low)//2
    if list1[mid]==target:
        print("exact match found")
        break
    elif list1[mid]<target:
        low=mid+1
    elif list1[mid]>target:
        high=mid-1
# insertion select
l1=[]

for i in range(1, len(l1)):
    key=l1[i]
    ip=i
    for j in range(i-1,-1,1):
        if l1[j]>key:
            l1[j+1]=l1[j]
            ip=j
        else:
            break
n= int(input())
l=[]
for i in range(n):
    N=input()
    l.append(N)
for i in range(1,len(l)):
    k=l[i]
    ip=i
    for j in range(i-1,-1,-1):
        if l[j]>k:
            l[j+1]=l[j]
            ip=j
        else:
            break'''

            
