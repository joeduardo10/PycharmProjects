from random import randint
print('=-' * 14)
print('  VAMOS JOGAR PAR OU IMPAR ')
print('=-' * 14)
vitoria = 0
while True:
    jogador = int(input('Digite o valor: '))
    computador = randint(0, 10)
    soma = jogador + computador
    impar_par = ' '
    while impar_par not in 'PpIi':
        impar_par = str(input('Par ou Impar [P/I] ')).strip().upper()[0]
    print('--' * 26)
    print(f'Você jogou {jogador} e o Computador jogou {computador} o total é {soma} ')
    print('Deu par' if soma % 2 == 0 else 'Deu Impar')
    print('--' * 26)
    if impar_par == 'P':
        if soma % 2 == 0:
            vitoria += 1
            print('''Você ganhou
 Vamos Jogar Novamente!''')
        else:
            print('Você perdeu!!! ...')
            break
        print('~~' * 26)
    elif impar_par == 'I':
        if soma % 2 == 1:
            vitoria += 1
            print('''Você ganhou
 Vamos Jogar Novamente!''')
        else:
            print('Você perdeu!!! ...')
            break
print(f'GAME OVER! Você venceu {vitoria} vezes. ')





