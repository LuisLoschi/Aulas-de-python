'''
1. Faça um programa que a soma de 3 números.
'''
x, y, z = 1, 2, 3

soma = x + y + z

print("soma é igual a: ", soma)

'''
2. Faça um programa que calcule a velocidade de um carro que andou uma distancia  de 500 metros em 20 segundos. 
Fórmula: Velocidade = distancia / tempo
'''
distancia = 500
tempo = 20

velocidade = distancia / tempo

print("Velocidade é igual a: ", velocidade, "m/s")


'''
3. Escreva um código que calcule a hipotenusa de um triângulo retângulo.
'''
co = float(input('Entre com o valor do cateto oposto: '))
ca = float(input('Entre com o valor do cateto adjacente: '))

hipotenusa = (ca ** 2 + co ** 2) ** (1/2)

print("\n**************************\n")

print("O valor da hipotenusa é: ", hipotenusa)

'''
4. Escreva um código que calcule a idade de uma pessoa
'''
ano_atual = int(input("Digite o ano atual: "))
ano_nasc = int(input("Digite o ano que você nasceu: "))

idade = ano_atual - ano_nasc

print("Sua idade é: ", idade, "anos")

'''
5. Escreva um código que calcule a Fórmula de Bhaskara
'''
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

print("Calculando...")

delta = (b ** 2) - 4 * a * c

x1 = (-b + delta ** (1/2)) / (2 * a) 

x2 = (-b - delta ** (1/2)) / (2 * a)

print("X1 será igual a:", x1, "e X2 será igual a: ", x2)