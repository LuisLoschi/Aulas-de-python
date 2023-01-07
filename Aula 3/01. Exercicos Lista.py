'''
1. Coloque a lista [5, 4, 3, 2, 1] em ordem crescente
'''
numero = [5, 4, 3, 2, 1] 
numero.sort()

print('Ordem crescente: ', numero)


'''
2. Faça um programa que imprima apenas os numero pares  e outra os números impares da lista de 0 a 10 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
numero = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

par = numero[::2]
impar = numero [1::2]

print('numeros pares: ', par)
print('numeros impares: ', impar)

'''
3. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma dos números.
'''
lista = [5, 10, 15, 20, 25]

soma = sum(lista)

print("Soma é igual a: ", soma)
