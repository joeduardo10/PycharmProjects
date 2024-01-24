valor = int(input('digite um valor:')),\
        int(input('digite um valor:')), \
        int(input('digite um valor:')),\
        int(input('digite um valor:'))
print(f'Voce digitou os valores {valor}')
print(f'o numero 9 apareceu {valor.count(9)}')
if  3 in valor:
    print(f'O valor tres esta na posição {valor.index(3)+1}')
else:
    print('O valor 3 não aparece em nenhuma posição')
print('Os valores pares foram: ')
for i in valor:
    if i % 2 == 0:
       print(i, end= ', ')







