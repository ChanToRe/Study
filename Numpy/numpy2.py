import numpy as np

#배열 (가로축으로) 합치기
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

array3 = np.concatenate([array1, array2]) #array1과 array2를 같은 행으로 합침

print(array3.shape) #데이터의 양 출력
print(array3)

#배열 형태 바꾸지
array4 = np.array([1, 2, 3, 4])
array5 = array4.reshape(2, 2) #reshape를 사용하여 array4의 형태를 2*2로 변형

print(array5)

#배열 세로축으로 합치기
array6 = np.arange(4).reshape(1, 4)
array7 = np.arange(8).reshape(2, 4)

array8 = np.concatenate([array6, array7], axis=0)

print(array8)

#배열 나누기
array9 = np.arange(8).reshape(2, 4)
left, right = np.split(array9, [2], axis=1)
print(left)
print(right)
