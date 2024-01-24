altura = float(input('Informe a sua altura:  '))
peso = float(input('Informe oseu peso: '))
imc = peso / (pow(altura, 2))
if imc > 40:
    print(' Seu IMC = {:.1f}  - OBESIDADE  MORBIDA'.format(imc))
elif imc >=30 and imc <40:
    print(' Seu IMC = {:.1f}  - OBESIDADE  '.format(imc))
elif imc >=25 and imc <30:
    print(' Seu IMC = {:.1f}  - SOBREPESO'.format(imc))
elif imc >= 18.5 and imc < 25:
    print(' Seu IMC = {:.1f}  - PESO  IDEAL'.format(imc))
else:
    print(' Seu IMC = {:.1f}  - ABAIXO DO PESO'.format(imc))
