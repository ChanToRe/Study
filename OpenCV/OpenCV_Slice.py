import cv2

image = cv2.imread("/Users/jch/Documents/GitHub/Study/OpenCV/Images/togi.jpg") #이미지 로드

slice_image = image.copy()  #image를 바로 사용할 경우 본 이미지가 변경되기 때문에 카피해서 사용
slice_image = image[100:600, 200:700]   #[높이(행, 너비(열] 형식으로 잘라낼 영역 설정

cv2.imshow("slice", slice_image)

cv2.waitKey(0)
cv2.destroyAllWindows()