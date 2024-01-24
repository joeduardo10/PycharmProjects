#Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo. Seu programa tem que realizar
# três contagens através da função criada:
#  a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada
def contador(ini, fim, passo):
    if ini <= fim:
        for cont in range(ini, fim, passo):
            print(cont)
    else:
         for cont in range(fim, ini, passo):
            print('2',cont)







i = int(input('digite o nr inicio: '))
f = int(input('digite o fim: '))
passo = int(input('digite o passo: '))
contador(i,f, passo)