vrnum = list()
pos = 0
for cont in range(0, 5):
    vrnum.append(int(input(f'Digite um valor na posição {cont}: ')))
print(f'Voce digitou {vrnum}')
for p, n in enumerate(vrnum):
    maxi = max(vrnum)
    mini = min(vrnum)
print(f'O maior valor sorteado foi {(maxi)} na posição{p}  ')
print(f'O menor valor sorteado foi {(mini)} na posição {p}')

