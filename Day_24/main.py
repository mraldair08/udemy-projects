#with open("my_file.txt") as  file:   # with se encarga de abrir y cerrar el arhivo
#    contents = file.read()
#    print(contents)

with open("newfile.txt", mode="w") as  file:  #mode r = read  -  w = write  - a = append solo agrega al texto existente
   file.write("\n New text")
   
with open ("new_file.txt", mode='w') as new:
   new.write(file)