import socket
import struct

host = "10.42.0.1"
port = 5001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((host, port))

print(f"UDP receiver listening on {host}:{port}")

while True:
    packet, address = sock.recvfrom(2048)

    if len(packet) < 8:
        print("Packet terlalu kecil")
        continue

    header = packet[:8]
    payload = packet[8:]

    frame_id, chunk_id, total_chunks = struct.unpack("!IHH", header)

    print(
        f"Received frame={frame_id}, "
        f"chunk={chunk_id + 1}/{total_chunks}, "
        f"size={len(payload)} bytes "
        f"from={address}"
    )
