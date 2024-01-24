from datetime import date
ano_atual = date.today().year
idade = int(input('Informe a sua idade: '))
print('Quem nasceu em {} tem hoje {} anos em {}'.format(idade, (ano_atual-idade),ano_atual))
if ano_atual - idade == 18:
    print('Voce deve se alistar esse ano ! {}'.format(ano_atual))
elif ano_atual - idade < 18:
    alist = (idade + 18)-ano_atual
    print('voce deverá se alistar em {} anos . em {}'.format(alist, (ano_atual+alist)))
elif ano_atual - idade > 18:
    alist = ano_atual - (idade + 18)
    print('Passou o tempo de alistamento em {} anos... era pra alistar em {}'.format(alist, (idade + 18)))



