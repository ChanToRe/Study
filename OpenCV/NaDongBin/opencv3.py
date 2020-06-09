import cv2
import matplotlib.pyplot as plt

image = cv2.imread('stupa.png')

#ROI : resion of interest
#관심있는 부분을 의미, 특정 이미지에서 유의미한 공간을 의미

#numpy slicing : ROI 처리 가능
roi = image[200:350, 50:200] #ROI처리할 부분

#ROI 단위로 이미지 복사
image[0:150, 0:150] = roi #ROI처리된 이미지가 출력될 부분
#공간의 크기가 일치해야함
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

#픽셀별 색상 다루기
image[:, :, 2] = 0 #R을 모두 0처리
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()