# Imagina-se que você e sua equipe foram contratados por uma empresa de logística que acabou de entrar no ramo. Essa empresa trabalha com encomendas de pequeno e médio porte e opera somente entre 3 cidades.

# O valor que a empresa cobra por objeto é dado pela seguinte equação:

#--------------- total=dimensões*peso*rota---------------

# Em que cada uma das variáveis que compõe o preço total é quantizada da seguinte maneira:

# dimensões (cm³)	            valor (R$) 
# Até 1000	                        10
# Entre 1001 e 10000	            20
# Entre 10001 e 30000	            30
# Entre 30001 e 100000	            50
# Acima 100000	Não é aceito

# peso(kg)	                multiplicador
# Até 0.1	                    1
# Entre 0.11 e 1	            1.5
# Entre 1.10 e10	            2
# Entre 10.1 e 30	            3
# Acima de 30	Não é aceito

# rota	                                                multiplicador
# RS - De Rio de Janeiro até São Paulo	                       1
# SR - De São Paulo até Rio de Janeiro	                       1
# BS -De Brasília até São Paulo	                               1.2
# SB - De São Paulo até Brasília	                           1.2
# BR - De Brasília até Rio de Janeiro	                       1.5
# RB - Rio de Janeiro até Brasília	                           1.5




print ('Bem Vindo a companhia de logistica do Jorge Luiz Garcia Huanaquiri')

volume = 0
peso = 0
rota = 0
#---------------Começo da função da dimensões------------------
def dimensoesObjeto():
    global volume
    while True:
        try:
            altura = float(input('Digite a comprimento do objeto (em cm³):'))
            comprimento = float (input('Digite o largura do objeto(em cm³):'))
            largura = float(input('Digite a altura do objeto (em cm³):'))
            volume = comprimento * largura * altura
            if volume == 0:
                print('Por favor, Digite um número maior que 0')
                continue
            elif volume < 1000:
                valor = 10
            elif  1000 <= volume <=   10000:
                valor = 20
            elif 10000 <= volume <= 30000:
                valor = 30
            elif 30000 <= volume <= 100000:
                valor = 50
            else:
                print ('O volume do objeto é (cm³):',volume)
                print ('Inválido! Volume acima do limite não permitido.')
                print("por favor entre com as dimensões desejado novamente")
                continue 
            break
        except ValueError:
            print ('Você digitou alguma dimensão do objeto com o valor não numérico.')
    print ('O volume do objeto é (cm³):',volume)
    return valor
#-----------------Fim da função de dimensão--------------------

#-----------------Começo da função de peso---------------------
def pesoObjeto():
    global peso
    while True:
        try:
            peso = float(input('Digite o peso do objeto (em kg):'))
            if volume == 0:
                print ('Por favor, Digite um número maior que 0')
                continue
            elif peso <= 0.1:
                peso = 1
            elif 0.1 <= peso < 1:
                peso = 1.5
            elif 1 <= peso < 10:
                peso = 2
            elif 10 <= peso < 30:
                peso = 3
            else:
                print('Peso acima do limite não permitido.')
                print('Por Favor digite novamente')
                continue
            break
        except ValueError:
            print ('Você digitou algum valor da dimensão não númerico.')

#-------------------Fim da função de peso----------------------

#------------------Começo da função de rota--------------------
def rotaObjeto():
    global rota 
    while True:
        print ('Escolha a rota:\n'
               '(Rs - Rio de Janeiro -> São Paulo\n)'
               'SR - São Paulo -> Rio de Janeiro\n'
               'BS - Brasilia -> Sãp Paulo\n'
               'SB - São Paulo -> Brasilia \n'
               'BR - Brasilia -> Rio de Janeiro \n'
               'RB - Rio de Janeiro -> Brasilia)')
        
        rota = input('>>')

        if rota in ['RS','SR']:
            rota = 1
        elif rota in ['BS','SB']: 
            rota = 1.2
        elif rota in ['BR', 'RB']:
            rota = 1.5
        else:
            print('Rota não existente.')
            print('Por favor digite novamente.')
            continue 
        break
#-------------------Fim da função de rota----------------------

#-------------------Responsavel para obter informações digitada pelo usuário----------------------
valor = dimensoesObjeto()
pesoObjeto()
rotaObjeto()
total = valor * peso * rota 

#-------------------Responsavel por obter Resulatdo----------------------
print (f'Valor total a ser pago: R${total} (Dimensões: {valor} * {peso} * {rota})')