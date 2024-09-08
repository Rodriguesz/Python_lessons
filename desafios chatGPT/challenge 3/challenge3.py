'''
Desafio: Calculadora de Fatorial Recursiva
Escreva uma função em uma linguagem de programação à sua escolha para calcular o fatorial de um número de forma recursiva. O fatorial de um número 
�
n é o produto de todos os inteiros positivos de 1 até 
�
n.

Requisitos:

Crie uma função chamada calcular_fatorial que aceite um número como argumento e retorne o fatorial desse número.
Implemente a função de forma recursiva.
Teste sua função com alguns valores diferentes para garantir que ela está calculando corretamente o fatorial.

Observações:

Certifique-se de que seu código esteja bem comentado.
Você pode usar qualquer linguagem de programação com a qual você se sinta confortável.
Boa sorte! Se precisar de ajuda ou esclarecimentos, não hesite em perguntar.
'''

def calcular_fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        fatorial = num
        while num > 1:
            num -= 1
            fatorial = fatorial * num
        return fatorial

num = int(input("Informe o número que deseja saber o fatorial: "))
fatoriall = calcular_fatorial(num)

print(f"O fatorial de {num} é: {fatoriall}")
