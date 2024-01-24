from random import randint
from time import sleep
print('=-=' * 20)
print(             'Pense em um numeroentre 0 e 5 vou tentar adivinhar'                )
print('=-=' * 20)
num_1 = randint(0, 5)
nr=int(input('Em que  numero eu pense ?  '))
print('PROCESSANDO ... ')
sleep(1)
if nr == num_1:
    print('Voce Acertou! incrivel')
else:
    print('voce errou kkk eu pensei {}'.format(num_1))
print('=-=' * 20)
#print('Voce Acertou! incrivel' if nr == num_1 else 'voce errou kkk eu pensei',num_1 ) # outra maneira
