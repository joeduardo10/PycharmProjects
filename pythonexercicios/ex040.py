n1 = float(input('informe a nota da primeira prova: '))
n2 = float(input('Informe a Segunda nota: '))
media = (n1 + n2)/2
print('primeira nota{:.1f}, Segunda nota {:.1f},  A media é de {:.1F}'.format(n1, n2, media))
if media >= 7.0:
    print('Voce foi APROVADO !')
elif media >= 5.0 and media < 7.0:
    print('Voce vai para RECUPERAÇÃO')
elif media < 5.0:
    print('Voce foi *-  R E P R O V A D O  -*')
