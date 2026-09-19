import socket

HOST = "10.42.0.1"
# HOST = "0.0.0.0"
PORT = 5001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"UDP reciver listening on {HOST}:{PORT}")

while True:
  data, address = sock.recvfrom(4096)
  print(
    f"Received from {address}: "
    f"{data.decode(errors='replace')}"
  )
