from random import randrange

numeroAleatorio = randrange(0, 50)

tentar = True

while tentar:
    resposta = int(input('Tente advinhar o número: '))

    if resposta == numeroAleatorio:
        print('Parabéns você acertou!')
        tentar = False
    elif numeroAleatorio < resposta:
        print('Número é menor')
    else:
        print('Número é maior')

