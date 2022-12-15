# 38. Write a Python program to display astrological sign for given date of birth.

dia = int(input("Insira o dia do seu nascimento: "))
mes = input("Insira o mês do seu nascimento (janeiro, fevereiro, etc.): ")

if mes == 'dezembro':
	signo = 'Sagitário' if (dia < 22) else 'Capricórnio'
elif mes == 'janeiro':
	signo = 'Capricórnio' if (dia < 20) else 'Aquário'
elif mes == 'fevereiro':
	signo = 'Aquário' if (dia < 19) else 'Peixes'
elif mes == 'março':
	signo = 'Peixes' if (dia < 21) else 'Áries'
elif mes == 'abril':
	signo = 'Áries' if (dia < 20) else 'Touro'
elif mes == 'maio':
	signo = 'Touro' if (dia < 21) else 'Gêmeos'
elif mes == 'junho':
	signo = 'Gêmeos' if (dia < 21) else 'Câncer'
elif mes == 'julho':
	signo = 'Câncer' if (dia < 23) else 'Leão'
elif mes == 'agosto':
	signo = 'Leão' if (dia < 23) else 'Virgem'
elif mes == 'setembro':
	signo = 'Virgem' if (dia < 23) else 'Libra'
elif mes == 'outubro':
	signo = 'Libra' if (dia < 23) else 'Escorpião'
elif mes == 'novembro':
	signo = 'Escorpião' if (dia < 22) else 'Sagitário'
print(f"Seu signo é {signo}.")