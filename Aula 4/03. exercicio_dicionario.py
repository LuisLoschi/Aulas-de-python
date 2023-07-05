'''
Escreva um programa que cadastre 4 nomes e idades de pessoas em um dicionário e mostre no final 
a lista de usuários cadastrados e a media da idade das pessoas cadastradas
'''

pessoa = dict()
soma = 0
totalPessoa = 4

for n in range(0, totalPessoa):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    
    soma += idade #soma as idades
    
    pessoa[nome] = idade #Adiciona no dicionário
    
mediaIdade = soma / totalPessoa

print(pessoa)
print(f"Média da idade das pessoas cadastradas é: {mediaIdade}")