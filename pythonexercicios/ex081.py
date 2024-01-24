lista = []
cont  = 0
while True:
    lista.append(input('Informe um Valor: '))
    cont += 1
    resp = ' '
    while resp not in 'SN':
         resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'Foram digitados {cont} valores')
lista.sort(reverse=True)
print(f'{lista}')
if '5' in lista:
    print('foi encontrado o valor 5')

