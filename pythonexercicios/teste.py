'''def leiaInt(a: str):
    while True:
        valor = input(a)
        if valor.isnumeric():
            return int(valor)
        else:
            print('\033[31mERRO! Digite um número válido\033[m')


n = leiaInt('Digite um valor: ')
print(f'Você acabou de digitar o número {n}')'''
def leiaInt(frase):
    num = input(frase)
    while not num.isdecimal():
        print('\033[31mERRO! Digite um número inteiro.\033[m')
        num = input(frase)
    num = int(num)
    return num


n = leiaInt('Digite um valor: ')
print(f'Você acabou de digitar o número {n}')

