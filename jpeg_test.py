import sys

import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera gagal dibuka")
    sys.exit()

ret, frame = camera.read()

if not ret:
    print("Gagal membaca frame")
    camera.release()
    sys.exit()

height, width = frame.shape[:2]

success, encoded = cv2.imencode(".jpg", frame)

if not success:
    print("Gagal melakukan JPEG encoding")
else:
    print("JPEG encoding berhasil")
    print(f"Size JPEG: {len(encoded)} bytes")
    print(f"Resolution: {width}x{height}")

camera.release()
