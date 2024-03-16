with open('archive.zip', 'rb') as file1:
  with open('archive2.zip', 'rb') as file2:
    print(file1.readlines() == file2.readlines())