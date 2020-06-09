import cv2

image = cv2.imread("/Users/jch/Documents/GitHub/Study/OpenCV/Images/togi.jpg", cv2.IMREAD_ANYCOLOR) #imread: 이미지를 읽어옴 / 경로 입력 / 다양한 모드를 사용하여 이미지들 읽어올 수 있음 -> 초기상태
cv2.imshow("Togi", image)   #이미지 출력

cv2.waitKey(0)  # 지속적으로 입력 상태를 받아옴
cv2.destroyAllWindows()