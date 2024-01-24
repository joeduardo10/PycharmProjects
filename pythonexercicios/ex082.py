lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite os valores:' )))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for v in lista:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('_=' * 30)
print(f'os valores informados foram {lista}')
print(f'os valores pares são: {pares}')
print(f'os valores impares são {impares}')
