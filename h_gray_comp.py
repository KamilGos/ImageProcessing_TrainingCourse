import cv2 as cv2
import copy
print("Starting algorithm")

cap = cv2.VideoCapture(2)
if cap.isOpened() == True:
    print("OK")

while True:
    _, frame = cap.read()
    copy_frame = copy.deepcopy(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hue,saturation,value = cv2.split(frame)
    gray = cv2.cvtColor(copy_frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('value',value)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


cap.release()
cv2.destroyAllWindows()