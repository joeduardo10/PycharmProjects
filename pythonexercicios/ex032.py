from datetime import date
ano = int(input('Que ano desja analisar? coloque .0. para analisar o ano atual  '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano de {} é Bissexto'.format(ano))
else:
    print('O ano de {} Não é Bissexto'.format(ano))
