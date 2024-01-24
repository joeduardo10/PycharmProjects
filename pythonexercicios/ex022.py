nome = str(input('Digite o nome da Pessoa: ')).strip()
print('nome em maiusculas',nome.upper())
print('nome em minusculas', nome.lower())
print('Seu nme tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

