import random
num_list = []
for num in range(0, 15):
    repetido = True
    numero = random.randint(1, 25)
    while repetido:
        if numero in num_list:
            numero = random.randint(1, 25)
        else:
            repetido = False
    num_list.append(numero)

print(sorted(num_list))
