frase = str(input('Digite uma frase: ')).strip().lower()
print('a letra a aparece  {} na frase'.format(frase.lower().count('a')))
print('a primeira letra .a. ocorre no caractere {}'. format(frase.find('a')+1))
print('a ultima letra .a. apareceu no caractere {}'.format(frase.rfind('a')+1))