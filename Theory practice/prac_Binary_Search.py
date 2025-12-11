def Binary_search(arr,x):
    low, high = 0,len(arr)-1
    while low<=high :
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]< x:
            low = mid+1
        elif arr[mid]>x:
            high = mid-1
    return -1 
print(Binary_search([2,3,4,5,6,7,8,9],4))       