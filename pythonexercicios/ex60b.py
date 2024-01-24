n = int(input('digite um numero inteiro: '))
cont = n
f = 1
print('Calculando {}! = '.format(n), end=' ')
while cont > 0:
    print('{}'.format(cont), end = ' ')
    print(' x 'if cont > 1 else ' = ', end = ' ')
    f *= cont
    cont -= 1
print('{}'.format(f))