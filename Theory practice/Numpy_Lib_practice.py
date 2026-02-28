import numpy as np
arr=np.array([1, 2, 3],ndmin=5)
print(arr)
print("Number of dimensions:", arr.ndim)
# accsesing the elements in 1 D array
'''import numpy as np
arr=np.array([1,2,3,4])
print(arr[0]+arr[3])'''
# accessing the elements in 2 D array
'''import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(arr[1,1])'''
# accessing the elements in 3 D array
'''import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr[0,1,1])'''
# negative indexing
'''import numpy as np
arr=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,21,3],[4,5,6],[7,8,9]]])
print(arr)
print(arr[-1,-3,-2])
'''
