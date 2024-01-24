matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = col3 = lin = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
    print()
print('-=' * 30)
for l in range(0, 3):
    col3 += matriz[l][2]
for c in range(0, 3):
    if c == 0:
        lin = matriz[1][c]
    elif matriz[1][c] > lin:
        lin = matriz[1][c]
print(f'a soma de todos os valores pares é {soma}')
print(f'A soma da 3ª coluna é de : {col3}')
print(f'O maior valor da 2ª linha é {lin}')
