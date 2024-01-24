from random import randint
nr = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for n in nr:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(nr)}')
print(f'O menor valor sorteado foi {min(nr)}')

