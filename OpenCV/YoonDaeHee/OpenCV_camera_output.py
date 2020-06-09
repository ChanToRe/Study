import cv2

capture = cv2.VideoCapture(0)   #카메라의 영상 받음
capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)   #너비 설정
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) #높이 설정

while True:
    ret, frame = capture.read() #ret은 카메라가 정상작동할 경우 True 반환 / 작동안할 경우 False 반환
    cv2.imshow("VideoFrame", frame) #imshow : 창에 출력
    if cv2.waitKey(1) > 0:  #어떤 키를 눌러도 while문 종료
    #if cv2.waitKey(1) == ord('키값'):  #'키값'을 누르면 while문 종료
        break

capture.release()   #카메라에서 받아온 메모리 해제
cv2.destroyAllWindows() #윈도우 창 닫기