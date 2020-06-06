import numpy as np

#단일 객체 저장 및 불러오기
array = np.arange(0,10)

np.save('save.npy', array) #저장

result = np.load('save.npy')
print(result)


#복수 객체 저장 및 불러오기
array1 = np.arange(0, 10)
array2 = np.arange(0, 20)

np.savez('saved.npz', array1=array1, array2=array2) #복수 객체 저장
data = np.load('saved.npz') #로드

result1 = data['array1'] #result1으로 담아서 출력하는 형태
result2 = data['array2'] #result2으로 담아서 출력하는 형태
print(result1)
print(result2)