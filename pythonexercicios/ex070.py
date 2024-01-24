totcompra = mais1000 = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Informe o nome do produto: ')).strip()
    preço = float(input('Informe o preço do produto: R$ '))
    cont += 1
    totcompra += preço
    if preço >= 1000:
        mais1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
         resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'o total da compra é R$ {totcompra:.2f}')
print(f'{mais1000:.2f} custam mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')
