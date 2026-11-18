print("-" * 5 + " EXERCÍCIO 4.4 " + "-" * 5)
salario = int(input("Salário do funcionário: "))

if salario > 1250:
    novo_salario = salario + (salario * (10 / 100))
else:
    novo_salario = salario + (salario * (15 / 100))

print(f"O novo salário é: R${novo_salario}")