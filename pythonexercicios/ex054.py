from datetime import date
maior =0
menor =0
ano_atual = date.today().year
for i in range (1, 8):
    ano_nasc = int(input('Digite o ano de Nascimento da  {}ª pessoa: '.format(i)))
    if ano_atual - ano_nasc < 18:
        menor += 1
    else:
        maior += 1
print('total de menores {}'.format(menor))
print('total de maiores {}'.format(maior))



