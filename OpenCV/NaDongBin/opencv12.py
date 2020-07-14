import cv2
import matplotlib.pyplot as plt

image = cv2.imread('digit_image.png') #이미지 로드
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #이미지 흑백 변환
ret, thresh = cv2.threshold(image_gray, 230, 255, 0) #임계값 설정 230 넘을 경우 255로
thresh = cv2.bitwise_not(thresh) #흑백 반전

plt.imshow(cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB))
plt.show()

contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0] #Contour를 검출하여 contours로 저장
image = cv2.drawContours(image, contours, -1, (0, 0, 255), 4) #검출한 윤곽을 표기, -1의 경우 전체

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

#contour를 포함하는 사각형을 그림
contour = contours[0]
x, y, w, h = cv2.boundingRect(contour) #cv2.boundingRect() 함수를 사용하여 x, y, w, h 값을 반환
image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3) #cv2.rectangle()함수를 사용하여 사각형으로 표시

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

#대략적인 형태의 coutour를 구함
contour = contours[0]
hull = cv2.convexHull(contour) #cv2.convexHull()함수를 사용하여 대략적인 형태를 구함
image = cv2.drawContours(image, [hull], -1, (255, 0, 0), 4) #cv2.drawContours(image, [hull], -1, (B, G, R), 두께)함수를 사용하여 표시

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

#근사치 contour를 구함
contour = contours[0]
epsilon = 0.01 * cv2.arcLength(contour, True) #최대 거리(클수록 Point개수 감소)
approx = cv2.approxPolyDP(contour, epsilon, True)
image = cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
징
#area : 면적 / length : 둘레 / moments : 특징
contour = contours[0]
area = cv2.contourArea(contour)
print(area)

length = cv2.arcLength(contour, True)
print(length)

M = cv2.moments(contour)
print(M)