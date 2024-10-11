lista_precos = [1500, 1000, 800, 2000]
total_imposto = 0 #acumulado

def calcular_imposto(preco):
  if preco <= 1000:
    imposto = preco * 0.1
  else:
    imposto = preco * 0.15
  print(f'Preço: {preco}, Imposto: {imposto}')
  return imposto

for preco in lista_precos:
  imposto = calcular_imposto(preco)
  total_imposto = total_imposto + imposto

print('Total de Imposto:', total_imposto)


