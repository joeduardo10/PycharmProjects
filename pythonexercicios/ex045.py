from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', "TESOURA")
computador = randint(0, 2)
print('''Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua Jogada ? '))
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO !!!')
print('=-' * 15)
print(' O computador Escolheu {}'.format(itens[computador]))
print(' O    Jogador    Jogou {} '.format(itens[jogador]))
print('=-' * 15)
if computador == 0: # computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada Invalida...')
elif computador == 1: # computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada Invalida...')
elif computador == 2: # computador jogou Tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada Invalida...')



