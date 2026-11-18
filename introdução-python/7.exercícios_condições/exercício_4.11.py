print("-" * 5 + " EXERCÍCIO 4.11 " + "-" * 5)

valor_casa = int(input("Digite o valor da casa: "))
salario = int(input("Digite o seu salário: "))
anos_pagar = int(input("Digite a quntidade de anos a pagar: "))

meses_pagar = int(anos_pagar * 12)

prestação = valor_casa / meses_pagar

print("-" * 26)

if prestação <= (salario * 0.30):
    print(f"A prestação mensal é de R${prestação:1.2f}")
    print("-- EMRPRÉSTIMO APROVADO --")
else:
    print(f"A prestação mensal é de R${prestação:1.2f}")
    print("A prestação não pode ser maior que 30% do salário.")
    print("-- EMRPRÉSTIMO NEGADO --")