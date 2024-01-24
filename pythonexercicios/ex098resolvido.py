from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'contagem de {i} até {f} de {p} em {p}')
    sleep(110)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}  ', end='', flush= True)
            sleep(0.3)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}  ', end='', flush= True)
            sleep(0.3)
            cont -= p
        print('FIM')


# programa principal
contador (1, 10, 1)
contador(10, 1, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem ')
ini = int(input('Digite o início:  '))
fim = int(input('Digite o fim:     '))
passo = int(input('Digite o passo: '))
contador(ini, fim, passo)