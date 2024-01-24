'''n = 1
while n != 0:
    n = int(input('digite um valor: '))
print('fim')'''
'''r = 'S'
while r == "S":
    n = int(input('digite um valor: '))
    r = str(input('Continuar  [S / N] ')).upper()
print('fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} numeros pares e {} impares'.format(par, impar))