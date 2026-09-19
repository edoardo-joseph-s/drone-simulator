import sys

import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera gagal dibuka")
    sys.exit()

ret, frame = camera.read()

if not ret:
    print("Gagal membaca fream")
    camera.release()
    sys.exit()

height, width = frame.shape[:2]

succes, encoded = cv2.imencode(".jpg", frame)

if not succes:
    print("Gagal melakuakn JPEG encoding")
else:
    print("JPEG encoding berhasil")
    print(f"Size JPEG: {len(encoded)} bytes")
    print(f"Resolution: {width}x{height}")

camera.release()
