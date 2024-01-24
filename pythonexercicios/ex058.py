from random import randint
from time import sleep
print('=-=' * 20)
print(             'Pense em um numeroentre 0 e 5 vou tentar adivinhar'                )
num_1 = randint(0, 10)
print('=-=' * 20)
cont = 0
while True:
    nr=int(input('Em que  numero eu pense ?  '))
    print('PROCESSANDO ... ')
    cont += 1
    sleep(1)
    if nr == num_1:
        print('Voce Acertou! incrivel foram {}'.format(cont))
        break
    else:
        print('voce errou kkk eu pensei {}'.format(num_1))
    print('=-=' * 20)