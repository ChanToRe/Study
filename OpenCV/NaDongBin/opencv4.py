import cv2
import matplotlib.pyplot as plt
#보간법(Interpolation) : 이미지를 늘리거나 했을 때 채우는 방법
#cv2.resize(image, dsize, fx, fy, interpolation)
#INTER_CUBIC : 사이즈를 크게 할 때 주로 사용
#INTER_AREA : 사이즈를 작게 할 때 주로 사용

image = cv2.imread('stupa.png')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) #matplotlib에서는 RGB로 처리하기 때문에 변환해줘야함
plt.show()

expand = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC) #2배
plt.imshow(cv2.cvtColor(expand, cv2.COLOR_BGR2RGB))
plt.show()
배
shrink = cv2.resize(image, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA) #0.8배
plt.imshow(cv2.cvtColor(shrink, cv2.COLOR_BGR2RGB))
plt.show