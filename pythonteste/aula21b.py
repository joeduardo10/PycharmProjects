def somar(a=0, b=0, c=0):  # =0  parametros opcionais
    """
    Faz a soma de tres valores e mostra o resultado na tela
    :param a: recebe o primeiro valor
    :param b: recebe o Segundo valor
    :param c: recebe o terceiro valor
    :return:
    """
    s = a + b + c
    print(s)


somar(3, 2, 5)
somar(8, 4)
somar()
somar(b=9, c=8)
