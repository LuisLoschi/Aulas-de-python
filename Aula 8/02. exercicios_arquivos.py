'''
1) Crie um arquivo onde pedimos ao usuário preencher o nome e a nota do aluno
'''

arq = open("inserir dados.txt", "w")   #Cria arquivo para escrita "w"

for linha in range(1, 3):
    nome= input(f"Digite o nome do {linha}° aluno: ")
    nota1= float(input(f"Digite a {linha}° nota: "))
    nota2= float(input(f"Digite a {linha}° nota: "))
    
    texto = f"{nome} {nota1} {nota2}\n"
    
    arq.write(texto) #Escreve o nome e as notas no arquivo

arq.close()


'''
2) Faça um programa que leia os dados do arquivo anterior
'''
arq = open("inserir dados.txt", "r")    #Abre arquivo como leitura "r"
dados = arq.readlines()                 #lê varias linhas

for linha in dados:
    lista_linha= linha.strip().split()  #strip tira qualquer caractere especial e o split transforma os itens em lista
    
    print(f"O aluno {lista_linha[0]} teve as notas {float(lista_linha[1])} e {float(lista_linha[2])}")

arq.close()