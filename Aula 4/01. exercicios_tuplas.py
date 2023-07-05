'''
1) Escreva um programa que analise a tupla 9 9 9 4 5 3 2 1 5 7 e mostre:
A)Quantas vezes apareceu o valor 9
B)Em que posição foi digitado o primeiro valor 3
'''

tupla = (9, 9, 9, 4, 5, 3, 2, 1, 5, 7)
    
valorNove = tupla.count(9)
valorTres = tupla.index(3) + 1

print(f"O valor 9 apareceu {valorNove} vezes \nO valor 3 apareceu na posição: {valorTres}")