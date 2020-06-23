import cv2 as cv2
print("Starting algorithm")

cap = cv2.VideoCapture(2)
if cap.isOpened() == True:
    print("OK")

while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hue,saturation,value = cv2.split(frame)

    cv2.imshow('hue',hue)
    cv2.imshow('saturation', saturation)
    cv2.imshow('value', value)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


cap.release()
cv2.destroyAllWindows()