'''Desafio: Verificador de Palíndromos
Escreva um programa em uma linguagem de programação à sua escolha para verificar se uma palavra é um palíndromo. 
Um palíndromo é uma palavra, frase, número ou outro sequência de caracteres que se lê da mesma forma para frente 
e para trás (desconsiderando espaços, pontuações e diferenciação entre maiúsculas e minúsculas).

Requisitos:

O programa deve aceitar uma entrada do usuário (por exemplo, através da linha de comando ou de uma interface simples) para a palavra que será verificada.
O programa deve ignorar espaços, pontuações e diferenciação entre maiúsculas e minúsculas ao verificar se a palavra é um palíndromo.
O programa deve exibir uma mensagem indicando se a palavra é um palíndromo ou não.
Exemplo:

Entrada: "A man, a plan, a canal, Panama!"
Saída: "A palavra é um palíndromo."'''


frase = input("Digite a frase: ")
caracteres_a_remover = ",-;."
frase = frase.replace(" ", "").translate(str.maketrans("", "", caracteres_a_remover))

frase_inversa = ""
for letter in range(len(frase)):
    frase_inversa += frase[-letter -1]

#? Solução do GPT
# frase_inversa = "".join(reversed(frase))

if frase == frase_inversa:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")