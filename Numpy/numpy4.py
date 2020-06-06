import numpy as np

#numpy 원소 정렬
array = np.array([5, 11, 6, 77, 23])
array.sort() #오름차순 정렬
print(array)
print(array[::-1]) #내림차순 정렬 : 오름차수로 정렬된 것을 역순으로 정렬

array1 = np.array([[5, 9, 10, 3, 1], [8, 3, 4, 2, 5]])
print(array1)
array1.sort(axis=0) #열을 오름차순으로 정렬
print(array1)