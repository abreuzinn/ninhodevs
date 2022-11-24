aluno = input("Insira o nome do aluno: ")
n1 = float(input("Insira a 1ª nota: "))
n2 = float(input("Insira a 2ª nota: "))
n3 = float(input("Insira a 3ª nota: "))
n4 = float(input("Insira a 4ª nota: "))
media = (n1+n2+n3+n4)/4

if media >= 7.0:
    print(f"O aluno {aluno} foi aprovado com uma média de {media}. Parabéns!")
else:
    print(f"O aluno {aluno} foi reprovado com uma média de {media}.")
