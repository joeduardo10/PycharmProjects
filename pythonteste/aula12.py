nome = str(input('Digite seu nome: '))
if nome == 'Eduardo':
    print('QUE NOME BONITO')
elif nome == 'Lucas' or nome =='Maria' or nome=='João' or nome =='Pedro':
    print('Seu nome é bem popular no Brasil ')
elif nome in 'Ana Claudia Celia Sandra ':
    print('QUE BELO NOME FEMININO !')
else:  # esle é opcional
    print('Seu nome é bem normal.')
print('tenha um bom dia {}'.format(nome))
