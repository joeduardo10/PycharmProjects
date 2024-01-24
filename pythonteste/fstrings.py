#DICA 1
faturamento = 1000
print(f"Faturamento: {faturamento}")
print()
#DICA 2  abrir arquivo
nome_arquivo = "vendas.txt"
caminho = r'D:\users\Eduardo\Documentos\python'
arquivo = open(f"{caminho}/{nome_arquivo}", "r")
print(arquivo.read())
arquivo.close()
print()
#DICA 3  Formatando com casa decimal
print(f"Faturamento: {faturamento:.2f}")
print()
#Formato Moeda
print(f"Faturamento: R${faturamento:,.2f}")
#Número fixo de dígitos
cpf = 11233344
print(f"CPF: {cpf:011}") # preenche com zeros a esquerda
#Percentual
margem_lucro = 0.27
print(f"Margem: {margem_lucro:.1%}")
#DATAS
from datetime import datetime
hoje = datetime.now()
print(f"Data: {hoje:%d/%m/%Y}, Horário: {hoje:%H:%M}")
#Só cuidado com textos com chaves {}
produto = 'iphone'
print(f"{{Produto: {produto}}}")
