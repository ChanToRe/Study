import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('stupa.png')


#이미지 위치 변경
#cv2.warpAffine(image, M, dsize) : 이미지의 위치를 변경
    #M : 변환 행렬
    #dsize : Manual Size
height, width = image.shape[:2] #행, 열, 각픽셀의 정보 중 행과 영 정보만 가져옴

M = np.float32([[1, 0, 50], [0, 1, 10]]) #변환 행렬 정의 : 1, 0, 이동할 값(X) / 0, 1, 이동할 값(Y)
dst = cv2.warpAffine(image, M, (width, height))

plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()