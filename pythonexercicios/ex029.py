vel = float(input('Velocidade: '))
print('=-=' * 5, 'Dirija com segurança', '=-=' * 5)
if vel > 80:
    exced = (vel-80)
    print('voce foi ultrapassou a velocidade  em {} km e sua multa é: R$ {:.2f} '.format(exced, exced * 7))
else:
    print('voce esta dentro do limite')
