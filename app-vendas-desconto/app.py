# Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X que vende em atacado. Uma das estratégias de vendas dessa empresa X é dar desconto maiores por unidade conforme a tabela abaixo:

# Quantidades	                Desconto
# Até 9	                        0% na unidade
# Entre 10 e 99	                5% na unidade
# Entre 100 e 999	            10% na unidade
# De 1000 para mais	            15%na unidade

print ("Bem vindo a loja do Jorge Luiz Garcia")
# Coleta de informações para executar o programa.
valorProduto = float(input("Entre com o valor do Produto: "))
qtdProduto = int (input("Entre com a quantidade do produto: "))
valorTotal = valorProduto * qtdProduto
desconto = ''

# Avaliações condicionais para análise do desconto.
if 0 <= qtdProduto <= 9: # if qtdPrdouto >=0 and qtdProduto <=9
  desconto = '(desconto de 0%)'
  valorFinal = valorTotal
elif 10 <= qtdProduto <= 99:
  desconto = '(desconto de 5%)'
  valorFinal = valorTotal - valorTotal * 0.05
elif 100 <= qtdProduto <= 999:
  desconto = '(desconto de 10%)'
  valorFinal = valorTotal - valorTotal * 0.10
else :
  desconto = '(desconto de 15%)'
  valorFinal = valorTotal - valorTotal * 0.15

# Impresão do resultado final.
print(f'O valor sem desconto foi de: R$ {valorTotal:.2f}')
print(f'O valor com desconto foi: R$ {valorFinal:.2f}')
print('Obteve', desconto)