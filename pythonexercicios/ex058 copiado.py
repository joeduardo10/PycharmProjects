from random import randint
comp = randint(0, 10)
print ('sou seu computador e acabei de pensar em um numero entre 0 e 10')
print('Voce consegue adivinhar qual foi?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print('mais  ...  tente mais uma vez!')
        elif jogador > comp:
            print('Menos  ... tente novamente!')
print('Acertou !!! com {} tentativas  '.format(palpite))
