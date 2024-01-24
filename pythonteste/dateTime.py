from datetime import datetime, timedelta

# data
hoje = datetime.now()
print(f' mostra dia de hoje--> {hoje}')
print(f' data no formato ano/mes/dia--> {hoje.date()}')
print(f' pega o dia --> {hoje.day}')
print(f' Pega o ano --> {hoje.year}')

# calculos com data - Variações de data
#Class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
amanha1 = hoje + timedelta(days=3) # + 3dias
amanha2 = hoje + timedelta(weeks=1)
print(f' soma mais 3 dias contando de hoje --> {amanha1}')
print(f' soma uma semana contando de hoje --> {amanha2}')

data_contrato = datetime(year=2022, month=10, day=2)
atraso = hoje - data_contrato #data futura gera nro negativo
print('', atraso)
print( f' mostra só em dias --> {atraso.days}')

#Extrair datas em outros formatos

data_contrato = "01/09/2022"
data_contrato = datetime.strptime(data_contrato, "%d/%m/%Y") # onde "%d/%m%Y"  é mascara
print(f' {data_contrato}')

# Formato Brasileiro
print(hoje.day,'/', hoje.month,'/', hoje.year) # + trabalhoso
print(hoje.strftime("%d/%m/%Y"))
print(hoje.strftime("%A")) #pega dia da semana mas sempre em inglês

# fuso horário
#hoje = hoje - timedelta(hours=1) # -1 hora
#print(hoje)

import zoneinfo
print(f' mostra o nome da zona {zoneinfo.available_timezones()}')
zona = zoneinfo.ZoneInfo('Europe/Copenhagen')
agora_copenhagen = hoje.astimezone(zona)
print(agora_copenhagen)