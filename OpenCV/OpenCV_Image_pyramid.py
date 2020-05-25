import cv2

image = cv2.imread("/Users/jch/Documents/GitHub/Study/OpenCV/Images/togi.jpg") #이미지 로드

height, width, channel = image.shape    #높이, 너비, 채널값 저장

#src = cv2.pyrUp(image, dstsize=(width*2, height*2), cv2.BORDER_DEFAULT)

pyramid_image1 = cv2.pyrUp(image)   #원본이미지 *2
pyramid_image2 = cv2.pyrDown(image) #원본이미지 1/2

#cv2.pyrup()과 cv2.pyrDown()의 픽셀 외삽법은 cv2.BORDER_DEFAULT만 사용 가능

cv2.imshow("image", image)
cv2.imshow("Up", pyramid_image1)
cv2.imshow("Down", pyramid_image2)

cv2.waitKey(0)
cv2.destroyAllWindows()