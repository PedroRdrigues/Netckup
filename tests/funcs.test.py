# import os


# def diretorio():
#   res = str(input(">>> ")); print('\n')
#   if os.path.isdir(res):
#     print(os.listdir(res))
#     print('\n===============================\n')
#     for i ,arq in enumerate(os.listdir(res)):
      
#       print(f"{i+1} => {bytes(arq.encode())}")
      
#       with open(f"{res}\\{arq}", "r") as file:
#         ...  
        




# if __name__ == "__main__":
#   diretorio()



# # print("Strings -> Bytes")
# # n = "pedro é o melhor de todos"
# # by = n.encode()
# # print(by)
# # print('===============================')
# # string = "Olá, mundo!"
# # by = string.encode()
# # print(by)
# # print('===============================')
# # string = "Olá, mundo!"
# # by = bytes(string, 'utf-8')
# # print(by)
# # print('===============================')
# # string = "Olá, mundo!"
# # by = bytearray(string, "utf-8")
# # print(by)
# # print('===============================')









# # print("List -> Bytes")
# # listBy = [1,2,3,4,5]
# # by = bytes(listBy)
# # print(by)
# # print('===============================')
# # listBy = [
# #   [1,2],
# #   [4,5]
# #   ]
# # for i, v in enumerate(listBy):
# #   by = bytes(v)
# #   print(f"{i} -> {by}")
  




dt = list()
s = 'FILE ASDLJALDFALDKFJAÇDKJÇKDJAÇKDJASLKÇD'

c = len(s.split(' '))
while True:
  if c==0:
    break
  d = [i for i in s.split(' ')]
  dt.append(d)
  print(dt,'\n')
  c-=1

for i in range(len(dt)):
  print(len(dt[i]), type(dt), f"-> {dt[i]}\n")