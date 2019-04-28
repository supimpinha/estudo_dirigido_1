#questão b)
import math

metros_a_pintar = int(input('Informe o tamanho a ser pintado (em metros):'))
litros_necessarios = (metros_a_pintar / 6)

galoes_necessarios = math.ceil(litros_necessarios / 3.6)
print ('Será necessário comprar', galoes_necessarios, 'galões')

preco_galoes = galoes_necessarios * 25
print("O valor total dos galões será de R$:", preco_galoes)
