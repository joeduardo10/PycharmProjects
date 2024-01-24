'''cont = 1
while cont <= 10:
    print(cont, '  ', end='')
    cont += 1
print('Acabou')'''
n = cont = s = 0
while True:
    n = int(input('digite um numero inteiro: '))
    if n == 999:
        break
    s += n
#print('A Soma vale {}'.format(s))
print(f'A soma vale {s}')

