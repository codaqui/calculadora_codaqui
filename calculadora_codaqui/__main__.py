from calculadora_codaqui.soma import somar_dois_numeros

print("Você quer somar 2 numeros, ou uma lista?")
print("1 - Somar dois números")
print("2 - Somar uma lista")
opcao = input()
if int(opcao) == 1:
  numero1 = input("Digite o primeiro numero: ")
  numero2 = input("Digite o segundo numero: ")
  print(f"O resultado da soma é {somar_dois_numeros(numero1, numero2)}")
elif int(opcao) ==2:
  pass
else:
  print("Opção não configurada, encerrando aplicação.")