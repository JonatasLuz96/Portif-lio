import requests

link =  "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

resposta = requests.get(link) 
dic_resposta = resposta.json() 

cotacao_dolar = dic_resposta["USDBRL"]
print("Cotação do Dólar:", cotacao_dolar["bid"])

cotacao_euro = dic_resposta["EURBRL"]
print("Cotação do Euro:", cotacao_euro["bid"])

cotacao_bitcoin = dic_resposta["BTCBRL"]
print("Cotação do BitCoin:", cotacao_bitcoin["bid"])