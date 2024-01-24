'''ercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar.'''
import datetime
from datetime import datetime
func = {}
func['nome'] = str(input('Digite o nome do funcionário: ')).strip()
ano_nasc = int(input('Informe o ano de nascimento: '))
func['idade'] = datetime.now().year - ano_nasc
func['CTPS'] = int(input("Carteira de Trabalho (0 não tem): "))
if func['CTPS'] != 0:
    func['ano_contratação'] = int(input('informe o ano de contratação: '))
    func['salario'] = float(input('informe o salario: '))
    func['ano_aposent'] = func['idade'] + ((func['ano_contratação'] + 35) - datetime.now().year)
print('_=' * 30)
for k, v in func.items():
    print(f'    - {k} tem valor {v}')

