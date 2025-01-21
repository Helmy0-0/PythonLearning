import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6]) 
# print(arr)
# output: [1 2 3 4 5 6]

zeroes = np.zeros([2, 2]) #2x2 matrix of zeroes
# print(zeroes)
# output: [[0. 0.]
#          [0. 0.]]

ones = np.ones([2, 2])  #2x2 matrix of ones
# print(ones) 
# output: [[1. 1.]
#          [1. 1.]]

range_arr = np.arange(1, 10, 2) #1 to 10 with a step of 2
# print(range_arr)
# output: [1 3 5 7 9]

linspace_arr = np.linspace(0, 1, 5) #0 to 1 with 5 elements
# print(linspace_arr)
# output: [0.   0.25 0.5  0.75 1.  ]

reshape = arr.reshape([2, 3]) #2x3 matrix from arr with reshaping
# print(reshape)
# output: [[1 2 3]
#          [4 5 6]]

arr2 = np.array([1, 2, 3])
expanded = arr2[:, np.newaxis] #expand the dimensions of arr2
# print(expanded)
# output: [[1]
#          [2]
#          [3]]

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# # print(a + b) #element-wise addition
# output: [5 7 9]

arr3 = np.array([4, 16, 25])
# print(np.sqrt(arr3)) #element-wise square root
# # output: [2. 4. 5.]
# print(np.sum(arr3)) #sum of all elements
# # output: 45
# print(np.mean(arr3)) #mean of all elements
# # output: 15.0
# print(np.max(arr3)) #maximum element
# # output: 25
# print(np.min(arr3)) #minimum element
# # output: 4

arr4 = np.array([10, 20, 30, 40, 50]) 
# print(arr4[0]) #first element
# # output: 10 
# print(arr4[1]) #second element
# # output: 20
# print(arr4[1:3]) #second to third element
# # output: [20 30]
# print(arr4[2:]) #third element onwards
# # output: [30 40 50]

reshaped = arr4.reshape(1,5) #reshaping arr4
print(reshaped)
