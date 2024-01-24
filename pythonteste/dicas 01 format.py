#dica 1
#numeros gigantes com underline
#faturamento = 1_000_000_000

#  dica 2  mostrar numeros em formato de moeda brasileira
# formatação pelo  format ou usando bibliotecas

faturamento = 1000000000
texto_faturamento = f'{faturamento:,.2f}'.replace(',', '_').replace('.', ',').replace('_', '.')


print(f'O faturamento foi de R$ {texto_faturamento}')

# Opção 2: Biblioteca locale
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') # outra opção de código:
"Portuguese_Brazil.1252"
texto_faturamento2 = locale.currency(faturamento, grouping=True,
symbol=True)
print(f'O faturamento foi de {texto_faturamento2}')

