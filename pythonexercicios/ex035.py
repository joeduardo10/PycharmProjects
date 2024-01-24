r1 = float(input('informe o primeiro segmento '))
r2 = float(input('informe o segundo segmento '))
r3 = float(input('informe o terceiro segmento '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acima PODEM FORMAR UM TRIANGULO')
else:
    print('os segmetos acima NÃO FORMAM UM TRIANGULO')
