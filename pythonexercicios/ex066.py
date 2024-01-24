n = cont = s = 0
print('  999 para fim  ')
while True:
    n = int(input('digite um numero inteiro: '))
    if n == 999:
        break
    cont += 1
    s += n
#print('A Soma vale {}'.format(s))
print(f'A soma vale {s}, foram digitados {cont}')