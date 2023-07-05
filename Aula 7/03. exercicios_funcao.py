'''
Crie um programa de uma calculadora usando funções
'''

#passo 1 - dar boas vindas
def welcome():
    print("=" * 30)
    print("Seja Bem-Vindo a calculadora!")
    print("=" * 30)

#passo 3 - funções das operações
def adicao(n1, n2):
    soma = n1 + n2
    return soma

def subtracao(n1, n2):
    sub = n1 - n2
    return sub

def multiplicacao(n1, n2):
    mul = n1 * n2
    return mul

def divisao(n1, n2):
    div = n1 / n2
    return div  
    
def calcular():
    #Passo 2 - Escolher números e o operador
    numero1 = float(input("Digite o primeiro número: "))
    operacao = input('''Qual operação desejada?
    [+] p/ adição
    [-] p/ subtração
    [*] p/ multiplicação
    [/] p/ divisão \n''')

    numero2 = float(input("Digite o segundo número: "))
    
    #Passo 4 - Definir operação
    if operacao == '+':
        resultado = adicao(numero1, numero2)
        print(f'Soma de {numero1} + {numero2} = {resultado}')
        
    elif operacao == '-':
        resultado = subtracao(numero1, numero2)
        print(f'Soma de {numero1} - {numero2} = {resultado}')
        
    elif operacao == '*':
        resultado = multiplicacao(numero1, numero2)
        print(f'Soma de {numero1} - {numero2} = {resultado}')

    elif operacao == '/':
        resultado = divisao(numero1, numero2)
        print(f'Soma de {numero1} / {numero2} = {resultado}')
        
    else:
        print('Erro :( - tente novamente')

#Programa principal chamando as funções
welcome()

calcular()