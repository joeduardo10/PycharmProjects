#Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores  passadoa... ')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
           maior = valor
        else:
             if valor > maior:
                maior = valor
        cont += 1
    print(f'foram informados {cont}\ne o maior valor informado foi {maior}')


# programa principal
maior(2, 9, 4, 10, 5)
maior(0, -1, 4)
maior(1, 2)
#maio(0)
maior(6)
maior()
