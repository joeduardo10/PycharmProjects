salario = float(input('Informe o Salario: R$ '))
if salario > 1250.00:
    novosal = salario +(salario * 10 / 100)     #* 1.10
else:
    novosal = salario + (salario * 15 / 100)    #* 1.15
print('O salario de R$ {:.2f} foi reajustado em R$ {:.2f} '.format(salario, novosal))

