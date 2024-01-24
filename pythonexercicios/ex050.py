soma = 0
cont = 0
for i in range(1, 7):
    n = int(input('Digite um numero inteiro: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma de {} nro pares é {}'.format(cont, soma))

