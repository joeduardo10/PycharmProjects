#Exercício Python 090: Faça um programa que leia nome e média
# de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
cad = {}
cad['nome'] = str(input('digite o nome: : '))
cad['media'] = float(input(f'digite a media do aluno {cad["nome"]}: '))
if cad['media'] >= 7:
    cad['situação']= 'Aprovado'
elif cad['media'] >= 5 and cad['media'] < 7:
    cad['media']= 'Recuperação'
else:
    cad['situação']= 'reprovado'
print('-=' * 30)
for k, v in cad.items():
    print(f'  - {k} é igual a {v}')
print('-----' * 5)
print(cad.keys())
print(cad.values())
print(cad.items())



