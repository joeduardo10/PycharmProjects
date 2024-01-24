import PySimpleGUI as sg
from cotacao import pegar_cotacoes

sg.theme('DarkGray4')
layout = [
    [sg.Text("Pegar Cotação de Moeda")],
    [sg.Input(key="nome_cotação")],
    [sg.Button("Pegar Cotação"), sg.Button("Cancelar")],
    [sg.Text("",key="Texto_cotação")]
   ]
Janela = sg.Window("Sistema de Cotações", layout)
while True:
    evento, valores = Janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break
    if evento == "Pegar Cotação":
        codigo_cotação = valores["nome_cotação"]
        cotação = pegar_cotacoes(codigo_cotação)
        Janela["Texto_cotação"].update(f"A Cotação do {codigo_cotação} é de R$ {cotação}")
Janela.close()

''' USD Dolar americano
    CAD Dolar Canadense
    EUR Euro
    GBP Libra esterlina
    ARS Peso Argentino
    BTC Bit coin
    LTC Lite coin
    JPY Tene Japones
    CHF Franco suisso
    AUD Dolar Australiano
    CNY Yuan Chines
    ETH Ethereum'''