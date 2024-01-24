#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D)
# Uma lista de pessoas com idade acima da média
cadastro = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Informe o nome: ')).strip()
    while True:
        pessoa['sexo'] = str(input('informe sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO por favor digite apema M ou F')
    pessoa['idade'] = int(input('informe a idade: '))
    soma += pessoa["idade"]
    cadastro.append(pessoa.copy())
    resp = ' '
    while resp not in 'SN':
         resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Foran cadastrados {len(cadastro)} pessoas')
media = soma / len(cadastro)
print((f'B) A média de idade é de {media:5.2f}'))
print('C) As mulheres cadastrdas foram:', end=', ')
for p in cadastro:
    if p['sexo'] in 'Ff':
         print(f'{p["nome"] }', "", end=' ')
print()
print('D) Lista das pessoas que estão acima da média de idade: ', end='')
for p in cadastro:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f' {k} = {v}  ', end='')
        print()
print('<< ENCERRADO  >>')
print(cadastro)

