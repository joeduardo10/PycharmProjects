mais18 = homens = fmenos20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
         sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        fmenos20 += 1
    resp = ' '
    while resp not in 'SN':
         resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'  * Maiores de 18 anos foram  {mais18}')
print(f'  * Foram cadastrados {homens} Masculinos')
print(f'  * Foram cadastradas {fmenos20} mulheres com menos de 20 anos')

