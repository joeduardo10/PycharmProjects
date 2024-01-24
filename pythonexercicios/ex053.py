frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()     # frase teste    o lobo ama o bolo
junto = ''.join(palavras)
inverso = ''
print('Voce Digitou a frase {} '.format(junto))
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(' O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
     print('Temos um palíndromo')
else:
     print('A Frase digitada não é um palíndromo')



