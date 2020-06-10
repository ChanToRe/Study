import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('stupa.png')

width, height = image.shape[0:2]

#이미지 회전
#cv2.getRotationMatrix2D(center, angle, scale) : 이미지를 회전
    #center : 축
    #angle : 회전 각도
    #scale : scale Factor
M = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 0.5)
dst = cv2.warpAffine(image, M, (width, height))

plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()
print(M)