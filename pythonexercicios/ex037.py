while True:
    nr = int(input('Degite um numero inteiro : '))
    print('-='*10)
    print('[1] Para Hexadecimal')
    print('[2] Para Octal')
    print('[3] Para Binario')
    print('[5] Para Sair')
    print('-=' * 10)
    opcao = str(input("escolha a opção: "))
    if opcao == '5':
        break
    elif opcao == '1':
        print(' {} em Hexadecimal é {}'.format(nr, hex(nr)[2:]))
    elif opcao == '2':
        print(' {} em Octal é {}'.format(nr, oct(nr)[2:]))
    elif opcao == '3':
        print('{} em Binario é {}'.format(nr, bin(nr)[2:]))
    else:
        print('opção invalida')
