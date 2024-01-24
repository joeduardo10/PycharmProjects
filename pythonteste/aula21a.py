#docstring
def contador(i, f, p):
    """
    --> Faz uma contagem na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    função criada po gustavo Guanabara do curso em video
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')


#contador(2, 10, 2)
help(contador)
