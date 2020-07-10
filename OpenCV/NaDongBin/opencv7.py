import cv2
import matplotlib.pyplot as plt

#이미지를 합치는 두 가지 방법
#cv2.add() : Saturation 연산 -> 0보다 작으면 0, 255보다 크면 255 : clip
#np.add() : Modulo 연산 -> 256은 0, 257은 1로 표현 -> 잘 사용하지 않음

image_1 = cv2.imread('stupa.png')
image_2 = cv2.imread('background.png')

#Saturation
result = cv2.add(image_1, image_2)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.show()

#Modulo
result = image_1 + image_2
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.show()