try:
    a = int(input('numerador: '))
    b = int(input('denominador: '))
    r = a / b
except(ValueError, TypeError):
    print('Infelizmente tivemos um problema com o tipo de dados digitado!!:(')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por Zero')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')

else:
    print(f'o resultado é {r:.1f}')
finally:
    print('Volte Sempre!')
