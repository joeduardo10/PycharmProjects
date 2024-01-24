v1 = int(input('digite o primeiro valor :'))
v2 = int(input('digite o Segundo valor :'))
opcao = ''
while opcao != '5':
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR''')
    opcao = str(input("escolha a opção: "))
    if opcao == '1':
        print('=-' *10)
        print('A Soma de {} e {} é {}'.format(v1, v2, (v1 + v2)))
        print('=-' * 10)
    elif opcao == '2':
        print('=-' * 10)
        print('A multiplicação de {} e {} é {}'.format(v1, v2, (v1 * v2)))
        print('=-' * 10)
    elif opcao == '3':
        if v1 == v2:
            print('=-' * 10)
            print('{}  e  {} são iguais '.format(v1, v2))
            print('=-' * 10)
        elif v1 > v2:
            print('=-' * 10)
            print('{} é Maior {}'.format(v1, v2))
            print('=-' * 10)
        else:
            print('=-' * 10)
            print('{} é menor {}'.format(v1, v2))
            print('=-' * 10)
    elif opcao == '4':
        v1 = int(input('digite o primeiro valor :'))
        v2 = int(input('digite o Segundo valor :'))
    elif opcao == '5':
        print('=-' * 10)
        print('obrigado por utilizar o programa')
        print('=-' * 10)
        opcao = '5'
    else:
        print('=-' * 10)
        print('opção Invalida !!')
        print('=-' * 10)





