n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda  nota: '))
media = (n1+n2)/2
print('A sua média foi: {:.1f}'.format(media))
print('Parabens!'if media >=6 else 'Estude mais')
'''if media >= 6:
    print('Sua media foi boa, PARARABENS!')
else:
    print('Sua media foi ruim ESTUDE MAIS!')'''