import socket

HOST = "192.168.100.73"
PORT = 5500

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CLIENT.connect((HOST, PORT)); print("Conectado...\n")

req = str(input(">>> "))
CLIENT.send(req.encode())

with open(req, "wb") as file:
  while True:
    data = CLIENT.recv(1_000_000)
    
    if not data:
      break
    
    file.write(data)
    
print(f">>> {req} recebido...")