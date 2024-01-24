'''Exercício Python 096: Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''
def area (l, c):
    s = l * c
    print(f'A area de um terreno de {largura} x {comprimento} é de  {s}')

def cabecalho():
    print('_' * 30)
    print('controle de terrenos')
    print('_' * 30)


cabecalho()
largura = float(input('informe a largura (m): '))
comprimento = float(input('Informe o comprimento(m): '))
area(largura, comprimento)