# 33. Write a Python program to convert month name to a number of days.

mes = input("Insira um mês (Janeiro, Fevereiro, etc.) e veja sua duração em dias: ")

if mes == "Fevereiro":
    print(f"{mes} possui 28 dias ou 29 dias em anos bissextos.")
elif mes in ("Abril", "Junho", "Setembro", "Novembro"):
    print(f"{mes} possui 30 dias.")
elif mes in ("Janeiro", "Março", "Maio", "Julho", "Agosto", "Outubro", "Dezembro"):
    print(f"{mes} possui 31 dias.")
else:
    print("Mês inválido.")