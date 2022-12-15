# 37. Write a Python program that reads two integers representing a month and day and prints the estacao for that mes and day.

mes = input("Insira um mês (Janeiro, Fevereiro, etc.): ")
day = int(input("Insira um dia: "))

if mes in ('Janeiro', 'Fevereiro', 'Março'):
	estacao = 'Inverno'
elif mes in ('Abril', 'Maio', 'Junho'):
	estacao = 'Primavera'
elif mes in ('Julho', 'Agosto', 'Setembro'):
	estacao = 'Verão'
else:
	estacao = 'Outono'

if (mes == 'Março') and (day > 19):
	estacao = 'Primavera'
elif (mes == 'Junho') and (day > 20):
	estacao = 'Verão'
elif (mes == 'Setembro') and (day > 21):
	estacao = 'Outono'
elif (mes == 'Dezembro') and (day > 20):
	estacao = 'Inverno'

print(f"A estação é {estacao}.")
