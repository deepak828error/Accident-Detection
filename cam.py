import cv2


cap = cv2.VideoCapture(r'C:\Users\dk466\OneDrive\Desktop\project\demovideo.mp4')

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(0) & 0xFF == ord('q'):
       cv2.destroyAllWindows()
    break