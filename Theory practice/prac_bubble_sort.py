# TIME COMPLEXITY for this Bubble sorting is in the Order of O(n^2)
 
def bubble_sort(list1):
    for i in range(len(list1)):
        for j in range(0,len(list1)-i-1):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
    return list1
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))

# question 1
def Bubble_sort():
    list1=list(map(int,input().split()))
    count=0
    print(list1)
    for i in range(len(list1)):
        for j in range(0,len(list1)-i-1):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
                count+=1
    return f'sorted list is : {list1}, count is {count}'
print(Bubble_sort())
 
 # Recursive manner of Bubble sort
def bubble_sort_recursive(arr, n=None, count=0):
    # Initialize n on first call
    if n is None:
        n = len(arr)

    # Base case: if only one element left, stop
    if n == 1:
        return arr, count

    # Perform one pass of bubble sort
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            count += 1

    # Recursive call for remaining n-1 elements
    return bubble_sort_recursive(arr, n-1, count)

# Example usage
marks = [45, 12, 78, 34, 56]
sorted_list, swaps = bubble_sort_recursive(marks)
print(f"Sorted list: {sorted_list}, Total swaps: {swaps}")
 
 # PASS BY PASS VISUALIZATION
def bubble_sort_visual(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f"After pass {i+1}: {arr}")

marks = [45, 12, 78, 34, 56]
bubble_sort_visual(marks)

# While LOOP BUBBLE SORT
def bubble_sort(arr):
    n = len(arr)
    count = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                count += 1
                swapped = True
        n -= 1  # reduce range since last element is sorted
    return arr, count

marks = [45, 12, 78, 34, 56]
print(bubble_sort(marks))

    