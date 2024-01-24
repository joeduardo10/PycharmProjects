opcao = ' '
sexo = ' '
mais18 = 0
homens = 0
fmenos20 = 0
while opcao != 'N':
    idade = int(input('Informe a idade: '))
    sexo = str(input('Masculino / Feminino [M/F] ')).strip().upper()[0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        fmenos20 += 1
    opcao = str(input('Deseja continuar[S/N]:')).strip().upper()[0]
print(f'  * Maiores de 18 anos foram  {mais18}')
print(f'  * Foram cadastrados {homens} Masculinos')
print(f'  * Foram cadastradas {fmenos20} mulheres com menos de 20 anos')