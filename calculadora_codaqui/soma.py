def somar_dois_numeros(x, y):
  return float(x) + float(y)

def somar_infinitos_numeros(lista_numeros: list):
  numero_final = 0
  for item in lista_numeros:
    numero_final += item
  return numero_final