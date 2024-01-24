# Dica 3 - if na mesma linha para situações simples
# Ex: bonus do funcionário:
# se vendeu mais do que 500, o bonus é de R$200
# se vendeu menos do que 500, o bonus é de R$50
faturamento = 1000
if faturamento > 500:
    bonus = 200
else:
    bonus = 50
print(bonus)
# fazendo agora tudo em 1 linha:
bonus = 200 if faturamento > 1000 else 50
# lembre de fazer isso apenas para casos simples de if, se não dificulta a leitura
print(bonus)