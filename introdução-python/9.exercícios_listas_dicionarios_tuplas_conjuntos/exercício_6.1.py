print("-" * 5 + " EXERCÍCIO 6.1 " + "-" * 5)

notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 1

while x <= 7:
    notas[x] = float(input(f"Nota {x}: "))
    soma += notas[x]
    x += 1

print("-" * 30)
x = 1

while x <= 7:
    print(f"Nota {x}: {notas[x]:6.2f}")
    x += 1

print(f"Média: {soma / x:7.2f}")