tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',\
         'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinza', 'dezeseis', 'dezesete',\
         'dezoito', 'dezenove', 'vinte')

while True:
    i = int(input('digite um numero entre 0 e 20: '))
    if 0 <= i <= 20:
        break
        print('Tente novamente', end=' ')
print(f'voce digitou o numero {tupla[i]}')








