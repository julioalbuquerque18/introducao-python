print("-" * 5 + " EXERCÍCIO 5.4 " + "-" * 5)

fim = int(input("Digite o último número a imprimir: "))
x = 0

while x <= fim:
    if x % 2 != 0:
        print(x)
    x = x + 1

print("-- FIM --")