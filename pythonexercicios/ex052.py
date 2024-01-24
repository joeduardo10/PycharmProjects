num = int(input('digite um numero: '))
tot = 0
for p in range(1, num + 1):
    if num % p == 0:
         print('\033[33m', end = ' ')
         tot += 1
    else:
          print('\033[31m', end = ' ')
    print('{} '.format(p), end=' ')
print('\n\033[m o numero {} foi dividido {} vezes'.format(num, tot))
if tot == 2:
    print('e por isso é numero primo')
else:
    print('e por isso não é primo')
