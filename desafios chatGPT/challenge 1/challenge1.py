"""Desafio: Análise de Dados Simples
Tarefas:
Obtenção dos Dados:

Crie uma lista de dicionários, onde cada dicionário representará uma pessoa com as seguintes informações:
Nome
Idade
Altura (em centímetros)
Peso (em quilogramas)
Análise de Dados:

Escreva funções para realizar as seguintes análises:
Média de Idades
Média de Alturas
Média de Pesos
Pessoa mais velha
Pessoa mais nova
Pessoa mais alta
Pessoa mais leve
Apresentação dos Resultados:

Exiba os resultados das análises de forma clara e organizada no console.
Manipulação de Dados:

Implemente uma função que permita adicionar uma nova pessoa à lista de dados."""

pessoas_dict =[
    {
        "nome":"Pedro",
        "idade": 22,
        "altura": 182,
        "peso": 85
    },
    {
        "nome":"Carla",
        "idade": 34,
        "altura": 162,
        "peso": 58
    },
    {
        "nome":"Vitor",
        "idade": 72,
        "altura": 176,
        "peso": 68
    },
]

total_altura = 0
total_idade = 0
total_peso = 0
mais_velho = pessoas_dict[0]["idade"]
mais_novo = pessoas_dict[0]["idade"]
mais_alta = pessoas_dict[0]["altura"]
mais_leve = pessoas_dict[0]["peso"]
for dictionary in pessoas_dict:
    total_altura += dictionary["altura"]
    total_idade += dictionary["idade"]
    total_peso += dictionary["peso"]
    
    if dictionary["idade"] > mais_velho:
        mais_velho = dictionary["idade"]
    if dictionary["idade"] < mais_novo:
        mais_novo = dictionary["idade"]
    if dictionary["altura"] > mais_alta:
        mais_alta = dictionary["altura"]
    if dictionary["peso"] < mais_leve:
        mais_leve = dictionary["peso"]
        
print(f"Média de idade: {round(total_idade/len(pessoas_dict), 2)}")
print(f"Média de altura: {round(total_altura/len(pessoas_dict), 2)}")
print(f"Média de pesos: {round(total_peso/len(pessoas_dict), 2)}")
print(f"Mais velho: {mais_velho}")
print(f"Mais novo: {mais_novo}")
print(f"Mais alto: {mais_alta}")
print(f"Mais leve: {mais_leve}")
        