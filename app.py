import cv2
import uuid

cam = cv2.VideoCapture(0)

cv2.namedWindow("ss app")
img_counter = 0

while True:
    ret, frame = cam.read()

    if not ret:
        print("failed")
        break
    cv2.imshow("test", frame)
    k = cv2.waitKey(1)

    if k % 256 == 27:
        print("escape")
        break
    elif k % 256 == 32:
        img_name = "opencv_frame_{}.png".format(str(uuid.uuid4())[:8])
        cv2.imwrite(img_name, frame)
        print("screenshot taken")
        img_counter += 1
        cv2.waitKey(100)

cam.release()
cv2.destroyAllWindows()