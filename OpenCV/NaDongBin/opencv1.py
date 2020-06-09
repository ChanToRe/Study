import cv2

img_basic = cv2.imread('stupa.png', cv2.IMREAD_COLOR)
cv2.imshow('img_basic', img_basic)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('result.png', img_basic)

img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)
cv2.imshow('img_gray', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('result2.png', img_gray)
