import cv2

import qr_extractor as reader

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    codes, frame = reader.extract(frame, True)
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print "I quit!"
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
