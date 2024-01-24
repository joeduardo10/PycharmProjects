valores = []
while True:
    n=(int(input('Informe o Valor:  ')))
    if n not in valores:
        valores.append(n)
        print('valor adicionado')
    else:
        print('Valor duplicado... não vou adicionar..')
    resp = ' '
    while resp not in 'SN':
         resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
valores.sort()
print("-=" * 30)
print(f'voce digitou os valores{valores}')


