import os

caminho = input(">>> ")  # Substitua pelo caminho da sua pasta
# caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
# arquivos = [arq for arq in caminhos if os.path.isfile(arq)]

# # Exemplo: Filtrando apenas arquivos .jpg
# zips = [arq for arq in arquivos if arq.lower().endswith(".zip")]


if os.path.isfile(caminho):
  print("é um arquivo")

  nome = caminho.split("/")
  print(len(nome))
  print(nome)
  nome = nome[-1]
  print(nome)
  

  # with open(nome, "r", encoding='utf-8') as file:
  #     # print(file)
  #     linesFile = "".join(file.readlines())
  # with open(f"BKP_{nome}", "w", encoding="utf-8") as newFile:
  #       newFile.write(linesFile)


elif os.path.isdir(caminho):
  # print("é um diretório")
  # print(os.listdir(caminho))
  listdir = os.listdir(caminho)
  for name in listdir:
    print(f"{caminho}/{name}: ")
    with open(f"{caminho}/{name}", "r", encoding='utf-8') as file:
      # print(file)
      linesFile = "".join(file.readlines())
      print(linesFile)
      print("\n")
      # print("".join(linesFile))
      with open(f"BKP_{name}", "w", encoding="utf-8") as newFile:
        newFile.write(linesFile)

  
else:
  print("Não Encontrado")

os.system("pause")
os.system("cls")