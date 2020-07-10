import cv2
import matplotlib.pyplot as plt

#cv2.threshold(image, thresh, max_vaule, type) : 임계값을 기준으로 흑/백으로 분류하는 함수
#thresh : 입계값 = 한계값 -> 이 한계값을 넘었을 때 어떤 식으로 처리할 것인가
image = cv2.imread('background.png', cv2.IMREAD_GRAYSCALE)

images = []
ret, thres1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
ret, thres2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
ret, thres3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
ret, thres4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
ret, thres5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
images.append(thres1)
images.append(thres2)
images.append(thres3)
images.append(thres4)
images.append(thres5)

for i in images:
  plt.imshow(cv2.cvtColor(i, cv2.COLOR_GRAY2RGB))
  plt.show()


#cv2.adaptiveThreshold(image, max_value, adaptive_method, type, block_size, C) : 이미지의 적음 임계점 처리
#adaptive_method : 임계값을 적절히 사용해서 처리하도록 하는 방법
#ADAPTIVE_THRESH_MEAN_C : 주변영역의 평균값으로 결정 -> 모든 값의 평균을 임계값으로 사용
#ADAPTIVE_THRESH_GAUSSIAN_C : 가우시안 필터 사용 -> 가우시안 윈도우 기반의 가중치들의 합에서 C를 뺀 값을 임계점으로 설정
ret, thres2_1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
thres2_2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 3)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))
plt.show()

plt.imshow(cv2.cvtColor(thres2_1, cv2.COLOR_GRAY2RGB))
plt.show()

plt.imshow(cv2.cvtColor(thres2_2, cv2.COLOR_GRAY2RGB))
plt.show()