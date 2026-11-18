print("-" * 5 + " EXERCÍCIO 3.11 " + "-" * 5)
preço = int(input("Preço da mercadoria: "))
desconto = int(input("Desconto do produto: "))

valor_final = preço - (preço * (desconto / 100))

print(f"O valor a pagar é: {valor_final}")