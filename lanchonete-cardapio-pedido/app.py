# Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma lanchonete. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.

# A lanchonete possui seguinte tabela de produtos listados com sua descrição, códigos e valores:

# Código	        Descrição	        Valor(R$)
# 100	        Cachorro-Quente	          9,00
# 101	      Cachorro-Quente Duplo	      11,00
# 102	            X-Egg                 12,00
# 103	           X-Salada	              13,00
# 104	           X-Bacon	              14,00
# 105	            X-Tudo	              17,00
# 200	        Refrigerante Lata	      5,00
# 201	          Chá Gelado	          4,00

acumulador = 0
#Descrição do lanche a ser pedido.
print("Bem vindo a lanchonete do Jorge Luiz Garcia")
print("**********Opção de Serviços**********")
print("| Código |        Descrição          | Valor |")
print("|  100   |     Cachorro-Quente       | 9,00  |")
print("|  101   |   Cachorro-Quente Duplo   | 11,00 |")
print("|  102   |          X-Xgg            | 12,00 |")
print("|  103   |         X-Salada          | 12,00 |")
print("|  104   |         X-Bacon           | 14,00 |")
print("|  105   |         X-Tudo            | 17,00 |")
print("|  200   |     Refrigerante Lata     | 5,00  |")
print("|  201   |        Chá Gelado         | 4,00  |")
while True:
# Coleta de código para um determinado pedido de lanche a ser feito.
  codigo = float (input("Digite o código desejado: "))
  if codigo == 100:
    acumulador = acumulador + 9
    print("Você pediu um cachorro quente no valor de 9,00")
  elif codigo == 101:
    acumulador = acumulador + 11
    print("Você pediu um cachorro-quente duplo no valor de 11,00")
  elif codigo == 102:
    acumulador = acumulador + 12
    print("Você pediu um X-Xgg no valor de 12,00")
  elif codigo == 103:
    acumulador = acumulador + 12
    print("Você pediu um X-Salada no valor de 12,00")
  elif codigo == 104:
    acumulador = acumulador + 14
    print("Você pediu um X-Bacon no valor de 14,00")
  elif codigo == 105:
    acumulador = acumulador + 17
    print("Você pediu um X-Tudo no valor de 17,00")
  elif codigo == 200:
    acumulador = acumulador + 5
    print("Você pediu um Refrigerante lata no valor de 5,00")
  elif codigo == 201:
    acumulador = acumulador + 4
    print("Você pediu um Chá gelado no valor de 4,00")
  # Correção caso de um código não existente.
  else:
    print("Código Inválido")
    continue
  #Opção se o cliente deseja continuar com seu pedido.
  resposta = input("Deseja continuar com seu pedido? (s/n): ")
  if resposta == "s":
    print("Então prossiga")
    continue
  #Impressão do resultado final
  else:
    print("Pedido finalizado")
    print(f"O valor final da conta é: R$ {acumulador: .2f}")
    break
