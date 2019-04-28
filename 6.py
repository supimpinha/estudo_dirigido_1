"6. Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem"

distancia = float (input("Informe a distância a ser percorrida:"))
velocidade = float (input("Informe a velocidade média em que o veículo estará:"))

tempo = distancia / velocidade

if tempo<1 :
    print ("O tempo será de:", tempo*60, " minutos")
else:
    print ("O tempo será de:", tempo, " horas")
