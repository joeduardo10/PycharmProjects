
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO!! digite um número inteiro válido. \033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário \033[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO!! digite um número inteiro válido. \033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário \033[m')
            return 0
        else:
            return n


num = leiaint('Digite um valor inteiro: ')
print(f'O Valor digitado foi {num}')
num = leiafloat('Digite um valor Real: ')
print(f'O Valor digitado foi {num}')
