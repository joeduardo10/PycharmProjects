print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('digite o primeiro termo: '))
razao = int(input('digite a razao da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}  --> '.format(termo), end='')
        termo += razao
        cont += 1
    print('-----PAUSA-----')
    mais = int(input('Quantos termos vc quer mostrar a mais: '))
    print('progressão finalizada com {} termos mostrados'.format(total))
print('FIM')
