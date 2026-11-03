#with open("my_file.txt") as  file:   # with se encarga de abrir y cerrar el arhivo
#    contents = file.read()
#    print(contents)

with open("newfile.txt", mode="w") as  file:  #mode r = read  -  w = write  - a = append
   file.write("\n New text")