from random import choice

def desenho_forca():
    print("  _______     ")
    print(" |/      |    ")

    if(chutes == 6):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(chutes == 5):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        
    if(chutes == 4):
        print(" |      (_)   ")
        print(r" |     \     ")
        print(" |            ")
        print(" |            ")

    if(chutes == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |       |     ")
        print(" |            ")

    if(chutes == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")


    if(chutes == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if(chutes == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

#Parte1: Criar arquivo com as palavras
arq = open("forca.txt", "r")
palavras = arq.readlines()
arq.close()

#Parte2: escolher palavras aleatórias
escolha = choice(palavras)
palavra = escolha.strip()
print(palavra)

#Apenas letras que podem ser digitadas pelo jogador 
alfabeto = list("abcdefghijklmnopqrstuvwxyz")
tentativas = []

#Parte6: variavel que equivale oas chutes
chutes = 6

#Parte7: contar número de letrar (SEM REPETIÇÂO) e somar com os chutes acertados
letrasPalavra = len(set(list(palavra)))
acertou = 0

while True:
    desenho_forca()
    #Parte6: mostrar valores
    print("Chutes: ", " ".join(tentativas))
    print("Você tem mais", chutes, "chances \n")      
    
    #Parte3: Criar linhas de acordo com a palavra escolhida
    #Parte5: Substituir a linha pela letra correta
    for letra in palavra:
        if letra in tentativas:
            print(letra, end= ' ')
        else:
            print("_", end= ' ')
    
    palpite = input("\nDigite seu palpite: ").lower()
    
    #Parte4: Tratativas de entrada do jogador
    if palpite not in alfabeto or palpite == '':
        print("Opa.. Isso não é uma letra! \n")
        continue
    elif palpite in tentativas:
        print("Hora hora... acho que essa letra já foi digitada! \n")
        continue
    tentativas.append(palpite)
    
    if palpite in palavra:
        print("Correto! \n")
        
        acertou += 1
        
    else:
        print("Errooou!\n")
        
        #Parte6: contagem regressiva
        chutes -= 1 
        
    #Parte6: chances acabaram
    if chutes == 0:
        desenho_forca()
        print("Você perdeu :/")
        break
    
    #Parte7: Conferir se acertos é o mesmo número de letras a serem chutadas
    if acertou == letrasPalavra:
        print("Parabéns, Você Ganhou!! :) - Sua palavra era: ", palavra.upper())
        break 
        
