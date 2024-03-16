import os
import socket


# Realiza a inicialização do servidor e aguarda a conexão do cliente.
def main():
  HOST = "192.168.100.73"
  PORT = 50501

  SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  SERVER.bind((HOST,PORT))
  SERVER.listen(); print(">>> Esperando conexão...\n")

  conn , addrs = SERVER.accept()

"""
Cria funções para receber a requisição e enviar uma resposta a partir dos códigos a baixo.
"""



inicio = conn.recv(1024).decode()
if inicio == 'init':
  res = 'archive.zip'

  if os.path.isfile(res):
    print(f">>> {res} requisitado...\n")
    
    with open(res, 'rb') as file:
      for data in file.readlines():
        conn.send(data)
      
      print(f"\n>>> {res} enviado...\n")

  elif os.path.isdir(res):
      print("\n>>> isso é um diretório!\n")

  else:
    print("\n>>> Dados não identificado!\n")

  print("\n>>> Fim...\n")
