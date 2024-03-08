import os
import socket


HOST = "192.168.100.73"
PORT = 5500

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((HOST,PORT))
SERVER.listen(1); print(">>> Esperando conexão...")

conn , addrs = SERVER.accept()

res = conn.recv(1024).decode()

if os.path.isfile(res):
  
  with open(res, 'rb') as file:
    for data in file.readlines():
      conn.send(data)
    
    print(f"\n>>> {res} enviado...")

elif os.path.isdir(res):
    print("\n>>> isso é um diretório!")

else:
  print("\n>>> Dados não identificado!")

print("\n>>> Fim...")
# os.system('pause')