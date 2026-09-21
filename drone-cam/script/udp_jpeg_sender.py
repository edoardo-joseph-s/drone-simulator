import socket
import struct
import sys

import cv2

# network configuration
gcs_ip = "10.42.0.1"
gcs_port = 5001
chunk_size = 1200

# open camera
camera = cv2.VideoCapture(1)

if not camera.isOpened():
    print("Gagal membuka camera")
    sys.exit()
print("Camera berhasil dibuka")

# capture one frame
ret, frame = camera.read()

if not ret:
    print("Gagal read frame")
    camera.release()
    sys.exit()

height, width = frame.shape[:2]

print(f"Resulution: {width}x{height}")

# jpeg encoding
success, encoded = cv2.imencode(".jpeg", frame)
if not success:
    print("JPEG encoding gagal")
    camera.release()
    sys.exit()

jpeg_data = encoded.tobytes()

print(f"JPEG Size: {len(jpeg_data)} bytes")

# split jpg into chunks
total_chunks = (len(jpeg_data) + chunk_size - 1) // chunk_size

print(f"Total chenks: {total_chunks}")

# create udp socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send chunks
frame_id = 1

for chunk_id in range(total_chunks):
    start = chunk_id * chunk_size
    end = start + chunk_size

    chunk = jpeg_data[start:end]

    header = struct.pack("!IHH", frame_id, chunk_id, total_chunks)

    packet = header + chunk

    sock.sendto(packet, (gcs_ip, gcs_port))

print("JPEG berhasil dikirimkan melaulai UDP")

# clean
sock.close()
camera.release()
