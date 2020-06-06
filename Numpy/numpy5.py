import numpy as np

#균일한 간격으로 데이터 생성
array = np.linspace(0, 10, 5) #0과 10 사이에 5개의 값을 넣어 초기화
print(array)

#난수의 재연 (실행마다 결과 동일)
np.random.seed(10) #seed를 사용해서 어떤 값을 기준으로해서 값을 생성할 것인지 설정
print(np.random.randint(0, 10, (2, 3))) #난수 생성

#numpy 배열 객체 복사
#잘못된 예 : 이 경우 array1의 값 또한 바뀌게
array1 = np.arange(0, 10)
array2 = array1
array2[0] = 99
print(array1)
print(array2)
#array1을 카피해서 사용해야 array1이 바뀌지 않음
array3 = np.arange(0, 10)
array4 = array3.copy()
array4[0] = 77
print(array3)
print(array4)