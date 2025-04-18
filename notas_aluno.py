a = float(input("Digite a primeira nota: "))
b = float(input("Digite a segunda nota: "))
c = float(input("Digite a terceira nota: "))

resultado = (a+b+c) / 3

if resultado >= 6:
    print(f"Aprovado, média: {resultado}")
else:
    print(f"Reprovado, média: {resultado}")

#entadas: a, b, c = 6, 7, 8
#saída = Aprovado, media: 7.0
