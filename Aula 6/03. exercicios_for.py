'''
1) Faça um programa que retorne a tabuada
'''
valor = int(input('digite valor da tabuada: '))

for numero in range(1,11):
    tabuada = valor * numero
    
    print(f'{valor} x {numero} = {tabuada}')


'''
2) Fazer um programa para encontrar todos os números pares entre 1 e 100
'''
print("Os números pares de 1 a 100 são: ")

for num in range(1, 101):
    if num % 2 == 0:
        print(num, end=" ")

