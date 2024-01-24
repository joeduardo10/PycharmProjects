print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('digite o primeiro termo: '))
razao = int(input('digite a razao da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{}  --> '.format(termo), end='')
    termo += razao
    cont += 1
print('-----FIM-----')