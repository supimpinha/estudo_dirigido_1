#questão c)

import math

metros_a_pintar = int(input('Informe o tamanho a ser pintado (em metros):'))
litros_necessarios = (metros_a_pintar / 6)

latas_necessarias = int(litros_necessarios / 18)
sobras = litros_necessarios % 18
galoes_necessarios = math.ceil(sobras / 3.6)
print ('Serão necessárias', latas_necessarias,"lata(s)")
print ("e", galoes_necessarios, "galões")

preco_galao_litro = galoes_necessarios * 25 + latas_necessarias * 80
print ("O valor total da compra será de: R$", preco_galao_litro)
