import cv2
print("Starting algorithm")

cascade = cv2.CascadeClassifier('faces2.xml')

cap = cv2.VideoCapture(0)
if cap.isOpened() == True:
    print("OK")

while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(frame)

    faces = cascade.detectMultiScale(v, 1.2, 4)

    for(x,y,w,h) in faces:
        cv2.rectangle(v, (x,y), (x+w, y+h), (255,255,255), 2)

    cv2.imshow('frame',v)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()



