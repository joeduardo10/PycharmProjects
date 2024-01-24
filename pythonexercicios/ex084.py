grupo = list()
pessoa = list()
maior_peso = list()
menor_peso = list()
mai = men = 0
#grupo = [['José', 92], ['Maria', 56], ['Antonio', 87], ['Pedro', 85], ['Eduarda', 78]]
while True:
    pessoa.append(str(input('nome: ')))
    pessoa.append(float(input('Peso:')))
    grupo.append(pessoa[:])
    pessoa.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=_' * 30)
print(f'Foram cadastradas {len(grupo)} pessoas ')
for i, p in enumerate(grupo):
    if i == 0:
        mai = men = p[1]
    else:
        if p[1] > mai:
            mai = p[1]
        if p[1] < men:
            men = p[1]
print(f'grupo{grupo}')
print(f'O maior peso foi de: {mai}')
for i in grupo:
    if i[1] == mai:
        print(f'As pessoas com o maior peso são: {i[0]}')
print('-' * 30)
print(f'O menor peso foi de : {men}')
for i in grupo:
    if i[1] == men:
        print(f'As pessoas com o menor peso são: {i[0]}')
