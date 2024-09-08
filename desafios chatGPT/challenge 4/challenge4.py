'''Desafio: Verificador de Números Primos
Escreva uma função em uma linguagem de programação à sua escolha para verificar se um número é primo ou não. 
Um número primo é aquele que é maior que 1 e não possui divisores além de 1 e do próprio número.

Requisitos:

Crie uma função chamada verificar_primo que aceite um número como argumento e retorne True se o número for primo, e False caso contrário.
Implemente a função de forma eficiente, evitando loops desnecessários.
Teste sua função com alguns valores diferentes para garantir que ela está verificando corretamente se um número é primo.'''

def verificar_primo(num):
    if num > 1:
        if num % 2 > 0 or num == 2:
            return True
        else:
            return False
    else:
        return False

num = int(input("Digite um numero: "))

if verificar_primo(num):
    print(f"O número {num} é primo!")
else:
    print(f"O número {num} não é primo!")
