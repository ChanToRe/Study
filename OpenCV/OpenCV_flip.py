import cv2

image = cv2.imread("/Users/jch/Documents/GitHub/Study/OpenCV/Images/togi.jpg") #이미지 로드
flip_image1 = cv2.flip(image, 0)    #cv2.flip(이미지, 값)으로 대칭 -> 0은 상하 대칭
flip_image2 = cv2.flip(image, 1)    #cv2.flip(이미지, 값)으로 대칭 -> 1은 좌우 대칭

cv2.imshow("togi.jpg", image)
cv2.imshow("flip1", flip_image1)
cv2.imshow("flip2", flip_image2)

cv2.waitKey(0)
cv2.destroyAllWindows()