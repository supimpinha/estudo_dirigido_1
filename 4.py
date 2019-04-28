"4. Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário."

salario = float (input("Informe o valor do salário:"))
porcentagem = float (input("Informe a porcentagem de aumento:"))

Salario_Atualizado = salario + ((salario * porcentagem)/100)
aumento = Salario_Atualizado - salario

print ("Valor do aumento", aumento, "reais")
