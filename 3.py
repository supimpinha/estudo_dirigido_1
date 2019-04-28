"3. Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos."

dias = int (input ("Forneça um número de dias:"))
horas = int (input("Forneça um número de horas:"))
minutos = int (input ("Forneça um número de minutos:"))
segundos = int (input ("Forneça um número de segundos"))
Total_em_segundos = (dias*24*60*60) + (horas*60*60) + (minutos*60) + (segundos)
print (dias,"dia(s),",horas,"hora(s),",minutos,"minuto(s), e",segundos,"segundo(s) representam:",Total_em_segundos,"segundo(s)")
