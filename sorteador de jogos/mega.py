import random
num_list = []
for num in range(0, 6):
    repetido = True
    numero = random.randint(1, 60)
    while repetido:
        if numero in num_list:
            numero = random.randint(1, 60)
        else:
            repetido = False
    num_list.append(numero)

print(sorted(num_list))
