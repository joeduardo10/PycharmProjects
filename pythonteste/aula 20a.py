def soma(a, b):
    s = a + b
    print(s)


#programa principal
soma(5, 4)
soma(9, 1)
soma(4, 8)
soma(1.13, 1.15)

def somar(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de a + b é {s}')

somar(b=5, a=9)
somar(55, 0)
print('__'* 30)

'''def contador(*num):
    print(num)

    
contador(5, 7, 3, 1, 4)
contador(8, 4, 7)'''


'''def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('  FIM')


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)'''


def contador(*num):
    tam = len(num)
    print(f'recebi os valores {num} e são ao todo {tam}')


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)





