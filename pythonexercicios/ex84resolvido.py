galera = list()
dado = list()
totmai = totmen =0
for i in range (0, 3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()
for i in galera:
    print(i[1])
    if i[1] >= 21:
        print(f'{i[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{i[0]} é menor de idade')
        totmen += 1
print(f'temos {totmai} maiores e {totmen} menores')
print(galera)