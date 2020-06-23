import cv2 as cv2
import copy
print("Starting algorithm")

cap = cv2.VideoCapture(2)
if cap.isOpened() == True:
    print("OK")

while True:
    _, frame = cap.read()

    blue = copy.deepcopy(frame)
    blue[:, :, 1] = 0
    blue[:, :, 2] = 0

    red = copy.deepcopy(frame)
    red[:, :, 0] = 0
    red[:, :, 2] = 0

    green = copy.deepcopy(frame)
    green[:, :, 0] = 0
    green[:, :, 1] = 0

    cv2.imshow('blue',blue)
    cv2.imshow('green', green)
    cv2.imshow('red', red)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
