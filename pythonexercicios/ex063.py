print('-' * 20)
print('Sequencia de Fibonacci')
print('-' * 20)
n = int(input('digite qts seguencia: '))
cont = 3
t1 = 0
print('{}... '.format(t1), end='')
t2 = 1
print('{}... '.format(t2), end='')
while cont <= n:
    t3 = t1 + t2
    print('{}... '.format(t3), end='')
    t1 = t2
    t2 = t3
    n -= 1
print('Fim')
print('-' * 20)

