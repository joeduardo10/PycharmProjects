op = int(input('digite opcoes de 1 a 5  : '))
def opcao1():
    print('1!!!')
    "Você selecionou a opção 1"
def opcao2():
    print('2 !!!')
    "Você selecionou a opção 2"
def opcao3():
    print('3 @@@@')
    "Você selecionou a opção 3"

opcoes = {1: opcao1, 2: opcao2, 3: opcao3}

opcoes.get(op)()


