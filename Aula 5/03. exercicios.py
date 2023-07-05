'''
1) Crie um programa para verifica se um número inteiro é par ou ímpar
'''
numero = int(input("Digite um número inteiro: "))

if (numero % 2 == 0):
    print("Número é par!")
else:
    print("Número é impar!")

'''
2) Crie um programa que possa realizar uma das 4 operações matemáticas adição, subtração, multiplicação e divisão
'''
#Escolher números
numero1 = float(input("Digite um número: "))
operacao = input("Digite a operação desejada: [+] [-] [x] [/] ") 
numero2 = float(input("Digite um número: "))

#condição
if (operacao == '+'):
    somar = numero1 + numero2
    print("Soma dos numeros é: " + " " + str(somar)) #Print com contatenação
    
elif (operacao == '-'):
    subtrair = numero1 - numero2
    print("Subtração dos numeros é: {0}".format(round(subtrair, 2))) #Print com .format

elif (operacao == 'x'):
    multiplicar = numero1 * numero2
    print(f"Multiplicação dos numeros é: {multiplicar:.2f}") #Print com f
    
elif (operacao == '/'):
    dividir = numero1 / numero2
    print("divisão dos numeros é: ", round(dividir, 2)) #Print com virgula
    
else:
   print("Erro ao digitar a operação :/")

'''
3) Faça um programa que pede duas notas de um aluno Em seguida ele deve calcular a média
do aluno e dar o seguinte resultado:
a) A mensagem "Aprovado" se a média alcançada for maior ou igual a sete
b) A mensagem "Reprovado" se a média for menor do que sete
c) A mensagem "Aprovado com Distinção", se a média for igual a dez
'''
#Escolher números
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10.0:
    print("Aprovado com Distinção !")
elif media >= 7.0 and media < 10:
    print("Aprovado !")
elif media < 7 and media <= 0:
    print("Reprovado !")
else:
    print("Erro :/")