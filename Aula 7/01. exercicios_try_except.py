'''
1) Crie um programa que faça a divisão de dois números digitados pelo usuário

a)Use try except com While para que o usuário digite um valor inteiro
b)Trateo erro ZeroDivisionError que indica que não pode dividir por zero
'''

while True:
    try:
        num1= float(input('Digite o primiero número: '))
        num2= int(input('Digite o segundo número: '))
        
        resultado = num1 / num2
    
    except ValueError:
        print('Erro - Digite um número inteiro \n')

    except ZeroDivisionError:
        print('Erro - Não é possível dividir por zero! \n')
      
    else:
        print('Resultado da divisão é: ', resultado)
        break