import sys

import cv2

camera = cv2.VideoCapture(1)

if not camera.isOpened():
    print("ERROR: Camera gagal dibuka")
    sys.exit()


print("Camera berhasil dibuka")
print("Push Q untuk exit")

while True:
    ret, frame = camera.read()

    if not ret:
        print("ERROR: Gagal membaca frame")
        break

    cv2.imshow("Drone camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
