import os
import socket


HOST = "192.168.100.73"
PORT = 5500

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CLIENT.connect((HOST, PORT)); print("Conectado...\n")

req = str(input(">>> "))
CLIENT.send(req.encode())

dt = []
while True:
  d = CLIENT.recv(1_000_000)
  if not d:
    break
  
  dt.append(d)

if not dt == []:
  with open(req, "wb") as file:
    for i in range(len(dt)):
      data = dt[i]
      
      if not data:
        break
      
      file.write(data)
      i+=1
      
    if os.path.exists(req):
      print(f">>> {req} recebido...")

else:
  print('>>> isso é um diretório!')
  
input(">>> ")