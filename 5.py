"5. Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar"

preco = float (input("Informe o preço:"))
porcentagem = float (input("Informe a porcentagem do desconto:"))

precoatualizado = preco - ((preco*porcentagem)/100)
desconto = preco - precoatualizado

print ("Valor do produto com desconto: R$", precoatualizado)
print ("Desconto: R$", desconto)
