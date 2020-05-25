import cv2

image = cv2.imread("/Users/jch/Documents/GitHub/Study/OpenCV/Images/togi.jpg") #이미지 로드

height, width, channel = image.shape    #높이, 너비, 채널값 저장
matrix = cv2.getRotationMatrix2D((width/2, height/2),90,1)  #회전의 중심점 설정 -> 너비의 절반과 높이의 절반 / 회전 각도 : 90 / 확대비율 : 1
Rotate_image = cv2.warpAffine(image, matrix, (width, height))   #회전 이미지를 선언 (원본이미지, 배열, (결과 이미지 넓이, 결과 이미지 높이))

cv2.imshow("image", image)  #원본 이미지 출력
cv2.imshow("Rotate_image", Rotate_image)    #회전 이미지 출력

cv2.waitKey(0)
cv2.destroyAllWindows()