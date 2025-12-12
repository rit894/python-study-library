#Selection Sort has a time complexity of O(n^2) in the best, average, and worst cases.
def Selection_sorting(a):
    for i in range(len(a)):
        min_index=i
        for j in range(i+1,len(a)):
          if a[j]<a[min_index]:
             min_index=j
        a[i],a[min_index]= a[min_index],a[i]

arr = [64, 25, 12, 22, 11]
Selection_sorting(arr)
print(arr)

# recursive format of this code 
def recursive_selection_sort(arr, start=0):
    # Base case: if start reaches the end of array, stop
    if start >= len(arr) - 1:
        return
    
    # Find the index of the minimum element in the remaining array
    min_index = start
    for j in range(start+1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    
    # Swap the found minimum with the current element
    arr[start], arr[min_index] = arr[min_index], arr[start]
    
    # Recursive call for the rest of the array
    recursive_selection_sort(arr, start+1)


# Example usage
arr = [64, 25, 12, 22, 11]
recursive_selection_sort(arr)
print("Sorted array:", arr)

# Function style (Using min and index)
def selection_sort_functional(arr):
    for i in range(len(arr)):
        # Find minimum in the unsorted part using built-in functions
        min_val = min(arr[i:])
        min_index = arr.index(min_val, i)
        arr[i], arr[min_index] = arr[min_index], arr[i]

# The selection sorting code using yeild
def selection_sort_steps(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        yield arr[:]   # yield current state of array
