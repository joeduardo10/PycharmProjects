n = 0
while True:
    if n < 0:
        print('--' * 15)
        print('Programa de tabuada encerrado')
        print('--' * 15)
        break
    print('--' * 15)
    n = int(input('Qual tabuada deseja mostrar? : '))
    print('--' * 15)
    for i in range (1, 11):
        print(f'{n} * {i} = {(n * i)}')


