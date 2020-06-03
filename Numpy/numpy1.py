import numpy as np

list_data = [1, 2, 3]
array = np.array(list_data) #Numpy는 기본적으로 파이썬의 기본 list와 호환이됨

print(array.size) #array의 사이즈 출력
print(array.dtype) #array의 자료형 출력
print(array[2]) #인덱싱 가능
print(array)

#0부터 3까지의 배열 만들기
array1 = np.arange(4) #0부터 4개를 채움
print(array1)

array2 = np.zeros((4,4), dtype=float) #4*4크기, 자료형은 float, zeros : 전부 0으로 채움
print(array2)

array3 = np.ones((3, 3), dtype=str) #자료형은 문자열도 가능
print(array3)

#0부터 9까지 랜덤 초기화된 배열 만들기
array4 = np.random.randint(0, 10, (3, 3)) #0부터 10사이의 숫자를 랜덤하게 3*3 크기로 배열
print(array4)

#평균이 0이고 표준편차가 1인 표준 정규를 띄는 배열
array5 = np.random.normal(0, 1, (3, 3)) #평균은 0, 표준편차는 1인 데이터를 랜덤하게 배열
print(array5)

