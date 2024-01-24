words = ('Agua', 'mole', 'Em', 'Pedra',
         'Dura', 'tanto', 'bate', 'ate',
         'que', 'fura')
for i in words:
    print(f'\nA Palavra {i.upper()}  temos: ',end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')