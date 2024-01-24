from datetime import date
print('-' * 35)
print(' CONFEDERAÇÃO NACIONAL DE NATAÇÃO ')
print('-' * 35)
ano = date.today().year
nascimeto = int(input('informe o ano de nascimento: '))
idade = ano - nascimeto
if idade <= 9:
    print('Voce tem {} anos e se enquadra na categoria  MIRIM'.format(idade))
elif  idade <=14:
    print('Voce tem {} anos e se enquadra na categoria  INFANTIL'.format(idade))
elif  idade <= 19:
    print('Voce tem {} anos e se enquadra na categoria  JUNIOR'.format(idade))
elif idade <= 25:
    print('Voce tem {} anos e se enquadra na categoria  SENIOR'.format(idade))
else:
    print('Voce tem {} anos e se enquadra na categoria  MASTER'.format(idade))
print('-' * 35)

