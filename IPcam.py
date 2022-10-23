import cv2

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print(f'width : {cap.get(3)}, height : {cap.get(4)}')

while(True):
    ret, cam = cap.read()

    if(ret):
        cv2.imshow('camere', cam)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()