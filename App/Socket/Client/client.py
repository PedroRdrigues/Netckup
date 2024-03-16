import os
import socket
import threading


# Tenta fazer a conexão no servidor e pede o que deve ser requisitado.
def main():
  HOST = "192.168.100.73"
  PORT = 50501

  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  try:
    client.connect((HOST, PORT)); print("Conectado...\n")
  except:
    print("Não foi possivel se conectar ao sevidor.\n")
    
    
    
# Envia a requisição para o servidor.
def send(client, req):
  try:
    print(f">>> {req} sendo requisitado.\n")
    
    client.send(req.encode())
    
  except:
    return
  
# Recebe a resposta do servidor.
def receive(client, res):
  dt = []
  
  while True:
    d = client.recv(1_000_000)
  
    if not d:
      break
      
    dt.append(d)

  if not dt == []:
    with open(res, "wb") as file:
      for i in range(len(dt)):
        data = dt[i]
        
        if not data:
          break
        
        file.write(data)
        
      if os.path.exists(res):
        print(f">>> '{res}' recebido.\n")

  else:
    print('>>> Não foi possivel localizar o item requisitado.\n')






main()