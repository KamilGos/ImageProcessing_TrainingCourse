import cv2

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture(2)
if cap.isOpened() == True:
    print("OK")

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )

    for(x,y,w,h) in boxes:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255,255), 2)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
