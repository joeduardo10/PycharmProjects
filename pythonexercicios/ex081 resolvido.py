valores = []
while True:
    valores.append(int(input('Informe um Valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-+=' * 30)
print(f'você digitou {len(valores)} valores')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print('5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')



