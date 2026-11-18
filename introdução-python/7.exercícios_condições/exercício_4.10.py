print("-" * 5 + " EXERCÍCIO 4.10 " + "-" * 5)
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

operação = input("Operação que deseja realizar: ")

if operação == "soma" or operação == "+":
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
elif operação == "subtração" or operação == "-":
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
elif operação == "multiplicação" or operação == "*":
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")
elif operação == "divisão" or operação == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
    else:
        print("Operação inválida.")
else:
    print("Operação inválida.")