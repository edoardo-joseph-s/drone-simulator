import socket
import struct

import cv2
import numpy as np

host = "0.0.0.0"
port = 5001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((host, port))

print(f"UDP receiver listening on {host}:{port}")

frames = {}

while True:
    packet, address = sock.recvfrom(2048)

    if len(packet) < 8:
        print("Packet terlalu kecil")
        continue

    header = packet[:8]
    payload = packet[8:]

    frame_id, chunk_id, total_chunks = struct.unpack("!IHH", header)

    if frame_id not in frames:
        frames[frame_id] = {"total_chunks": total_chunks, "chunks": {}}

    frames[frame_id]["chunks"][chunk_id] = payload

    received_chunks = len(frames[frame_id]["chunks"])

    print(f"Frame {frame_id}: {received_chunks}/{total_chunks} chunks")

    if received_chunks == total_chunks:
        print(f"Frame {frame_id} lengkap")

        frame_data = b"".join(
            frames[frame_id]["chunks"][i] for i in range(total_chunks)
        )

        image_array = np.frombuffer(frame_data, dtype=np.uint8)

        frame = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        if frame is None:
            print("ERROR: JPEG gagal di-decode")
        else:
            print("JPEG berhasil di-decode")

            cv2.imshow("GCS - Drone Camera", frame)

            cv2.waitKey(1)

            del frames[frame_id]
