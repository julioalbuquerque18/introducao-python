print("-" * 5 + " EXERCÍCIO 3.10 " + "-" * 5)
salario = int(input("Valor do salário: "))
aumento = int(input("Porcentagem de aumento: "))

salario_final = salario + (salario * (aumento / 100))

print(f"O salário final é: {salario_final}")