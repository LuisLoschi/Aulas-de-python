'''
1) Escreva um programa que leia a lista de números e evite que eles se repitam
'''

lista = [1, 1, 1, 1, 55, 55, 2, 2, 2, 3, 4, 4, 4, 55, 55, 55, 78, 78, 90, 90]

print(set(lista))

'''
2) Escreva um programa que leia 10 números e evite que eles se repitam
'''

lista2 = []

for i in range(1, 11):
    lista2.append(int(input(f"Digite o {i} numero: ")))

print(set(lista2))