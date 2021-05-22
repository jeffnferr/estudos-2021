nota1 = float(input("digite nota da av1 "))
nota2 = float(input("digite nota da av2 "))
media = (nota1+nota2)/2

if media >= 6.0:
    print(f"o aluno foi aprovado com a media {media}")
    print("faltou excessivamente")
else:
    print(f"o aluno foi reprovado com a media {media}")