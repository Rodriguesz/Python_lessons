# file = open("Day_24/my_file.txt")
# content = file.read()
# print(content)
# file.close() #!sempre fechar os arquivos abertos

#ou vc pode usar o with
#agr ele fecha sozinho
#? apenas leitura de arquivos
# with open("Day_24/my_file.txt") as file:
#     content = file.read()
#     print(content)

#?apaga todo o texto antigo e escreve o novo
# with open("Day_24/my_file.txt", mode= "w") as file:
#     file.write("New text.")

#? adiciona o novo texto mantendo o antigo
# with open("Day_24/my_file.txt", mode= "a") as file:
#     file.write("\nNew text.")

#? tbm cria o arquivo caso ele não exista
# with open("Day_24/new_file.txt", mode= "w") as file:
#     file.write("\nNew text.")

# with open("C:/Users/venom/OneDrive/Área de Trabalho/teste.txt") as file:
#     content = file.read()
#     print(content)

with open("../teste.txt") as file:
    content = file.read()
    print(content)