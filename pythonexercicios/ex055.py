maior = 0
menor = 0
for p in range (1, 6):
    peso=float(input('Degite o peso da {}ª pessoa:'.format(p)))
    if peso > maior:
        maior = peso
    else:
        menor = peso
print('O maior peso foi {}'.format(maior))
print('O menor peso foi {}'.format(menor))
