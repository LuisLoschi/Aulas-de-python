'''
1)Faça um programa que pede a senha ao usuário, e só sai do looping quando digitar a senha correta
'''

#Definir senha
senhaCorreta= 'fatec123'

#Entrada de dado
senhaDigitada = input('Digite a senha: ')

#Enquanto a senha for diferente da correta
while senhaCorreta != senhaDigitada:
    print('Senha incorreta !')
    
    #Faz nova tentativa
    senhaDigitada = input('Digite a senha: ')
    
print('Senha correta, acesso válido :)')

'''
2) Faça um programa que receba a idade de 10 pessoas e que calcule e mostre a quantidade de
pessoas com idade maior ou igual a 18 anos assim como a média das idades
'''

count= 1         #Variavel que armazena contagem
maiorIdade= 0    #Variavel que armazena quem é maior de idade
mediaIdade= 0    #Variavel que armazena a soma das idades para fazer a média
numPessoas= 10   #Variavel que armazena total de pessoas 
 
while count <= numPessoas:
    idadePessoa = int(input(f'Digite a idade da {count}° pessoa: '))
    
    mediaIdade += idadePessoa
    
    count += 1
    
    if idadePessoa >= 18:
        maiorIdade += 1
        
media = (mediaIdade / numPessoas)    
        
print(f'Quantidade de pessoas maiores de 18 anos: {maiorIdade}')
print(f'Média de idade da turma: {media}')

'''
3) Faça um programa que receba numero de alunos pelo usuário e calcule a média de uma turma
'''