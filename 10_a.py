#questão a)

import math

metros_a_pintar = int(input('Informe o tamanho a ser pintado (em metros):'))
litros_necessarios = (metros_a_pintar / 6)


latas_necessarias = math.ceil(litros_necessarios / 18)
print ('Será necessário comprar', latas_necessarias, 'lata(s)')

preço_lata = latas_necessarias * 80
print ("O valor total da(s) lata(s) será de R$:", preço_lata)







