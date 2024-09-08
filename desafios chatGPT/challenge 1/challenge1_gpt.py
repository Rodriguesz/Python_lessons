def calcular_medias(pessoas):
    total_altura = sum(pessoa["altura"] for pessoa in pessoas)
    total_idade = sum(pessoa["idade"] for pessoa in pessoas)
    total_peso = sum(pessoa["peso"] for pessoa in pessoas)

    media_idade = round(total_idade / len(pessoas), 2)
    media_altura = round(total_altura / len(pessoas), 2)
    media_peso = round(total_peso / len(pessoas), 2)

    return media_idade, media_altura, media_peso

def encontrar_extremos(pessoas):
    mais_velho = max(pessoa["idade"] for pessoa in pessoas)
    mais_novo = min(pessoa["idade"] for pessoa in pessoas)
    mais_alto = max(pessoa["altura"] for pessoa in pessoas)
    mais_leve = min(pessoa["peso"] for pessoa in pessoas)

    return mais_velho, mais_novo, mais_alto, mais_leve

def apresentar_resultados(medias, extremos):
    media_idade, media_altura, media_peso = medias
    mais_velho, mais_novo, mais_alto, mais_leve = extremos

    print(f"Média de idade: {media_idade}")
    print(f"Média de altura: {media_altura}")
    print(f"Média de peso: {media_peso}")
    print(f"Pessoa mais velha: {mais_velho}")
    print(f"Pessoa mais nova: {mais_novo}")
    print(f"Pessoa mais alta: {mais_alto}")
    print(f"Pessoa mais leve: {mais_leve}")

pessoas_dict = [
    {"nome": "Pedro", "idade": 22, "altura": 182, "peso": 85},
    {"nome": "Carla", "idade": 34, "altura": 162, "peso": 58},
    {"nome": "Vitor", "idade": 72, "altura": 176, "peso": 68},
]

medias = calcular_medias(pessoas_dict)
extremos = encontrar_extremos(pessoas_dict)
apresentar_resultados(medias, extremos)