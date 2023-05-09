import numpy  as np


# def print_array(arr):
#     print(arr.dtype)
#     print(arr)
#     print(arr.strides)
#     print()
# myarray = np.array([[1,2,3],[4,5,6]])
# print_array(myarray)

# myarrayT = myarray.T
# print_array(myarrayT)

# myarray2 = np.array([[1,4],[2,5],[3,6]])
# print_array(myarray2)

given_list=[1,2,3,4,5,6]
N,M=2,3

arr=np.array(given_list)
#*step1
arr1=arr.reshape((N,M))
print(arr1)
#*step2
arr2=arr1.reshape(M,N)#! 思考为什么
print(arr2)
#*step3
print(arr1.T)
print(arr1.transpose())