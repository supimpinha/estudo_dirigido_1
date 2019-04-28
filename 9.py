"9. Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias"

cigarros_dias = int (input("Informe a quantidade de cigarros consumidos por dia:"))
anos_fumados = int (input("Informe a quantos anos você fuma:"))


total_cigarros = (anos_fumados * 365) * cigarros_dias
dias_perdidos = (total_cigarros * 10)/ 1440


print ("Você perderá:", dias_perdidos, "dias de vida")
