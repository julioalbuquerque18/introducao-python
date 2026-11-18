print("-" * 5 + " EXERCÍCIO 4.3 " + "-" * 5)
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 & num3:
    num_maior = num1
if num2 > num1 & num3:
    num_maior = num2
if num3 > num1 & num2:
    num_maior = num3
print(f"O maior número é {num_maior}")

if num1 < num2 & num3:
    num_menor = num1
if num2 < num1 & num3:
    num_menor = num2
if num3 < num1 & num2:
    num_menor = num3
print(f"O menor número é {num_menor}")