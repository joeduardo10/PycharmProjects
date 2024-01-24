'''Crie um programa onde o usuário possa digitar
sete valores numéricos e cadastre-os em uma lista única que mantenha separados
 os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''
sete = []
par = []
impar = []
for val in range(1, 8):
    n = int(input(f'digite o {val} valor:'))
    if n % 2 == 0:
        par.append(n)
        par.sort()
    else:
        impar.append(n)
        impar.sort()
sete = par[:] + impar[:]
print(par)
print(impar)
print(sete)
