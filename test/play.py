import cv2

video_capture = cv2.VideoCapture('../unlabeled/8.hevc')

while True:
    
    ret, frame = video_capture.read()
    if not ret:
        break
    
    cv2.imshow('HEVC Video', frame)
    print(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

 
   
video_capture.release()
cv2.destroyAllWindows()