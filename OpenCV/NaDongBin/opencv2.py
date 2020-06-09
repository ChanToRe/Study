import cv2
import time
import matplotlib.pyplot as plt

image = cv2.imread('stupa.png')

#픽셀 수 및 이미지 크기 확인
print(image.shape) #픽셀 수
print(image.size) #크기

px = image[100, 100] #이미지 numpy 객체의 특정 픽셀을 가리킴

#B G R 순서로 출력
#Gray Scale인 경우 구분되지 않음
print(px)

#R값만 출력
print(px[2]) #B : 0 / G : 1


#특정 범위 픽셀 변경
#1 비효율적
start_time = time.time()
for i in range(0, 100):
    for j in range(0, 100):
        image[i, j] = [255, 255, 255]
print("---- %s second ----" %(time.time() - start_time))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show

#2 효율적 : 슬라이싱 사용
start_time = time.time()
image[0:100, 0:100] = [255, 255, 255]
print("---- %s second ----" %(time.time() - start_time))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show