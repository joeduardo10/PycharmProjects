print('==' * 20)
print('{:^38}'.format('BANCO GUANABARA'))
print('==' * 20)
valor = int(input('Que valor quer sacar? R$ '))
total = valor
cedula = 50
totcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
             print(f'total de {totcedula} cedulas de {cedula} R$')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0
        if total == 0:
            break
print('==' * 20)
print('{:^38}'.format('VOLTE SEMPRE AO BANCO GUANABARA'))
print('==' * 20)











