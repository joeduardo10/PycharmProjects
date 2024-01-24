print('=' * 22)
print('  10 TERMOS DE UMA PA   ')
print('=' * 22)
primeiro = int(input('primeiro termo: '))
razao = int(input('         razão: '))
decimo = primeiro + (10-1) * razao
for i in range(primeiro, decimo + razao, razao):
    print('{}'.format(i), end = ' -> ' )
print('ACABOU')