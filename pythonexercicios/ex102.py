#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(n, show = False):
    '''
    --> Calcula o Fatorial de um numero
    :param n: o numero a ser Calculado
    :param show: opcional (mostrar ou não a conta)
    :return: valor do fatorial de um numero n
    '''
    f = 1
    for c in range(n, 0, -1): # contando regressivamente
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#programa principal
print(fatorial(5, show=True))
print(fatorial(6,show=False))
print(fatorial(7))
help(fatorial)
