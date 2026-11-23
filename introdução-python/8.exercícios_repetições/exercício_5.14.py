print("-" * 5 + " EXERCÍCIO 5.14 " + "-" * 5)

soma = 0
quantidade = 0

while True:
    valor = int(input("Digite um valor para somar ou 0 para sair: "))

    if valor == 0:
        média = soma / quantidade
        break

    soma = soma + valor
    quantidade += 1

print("-" * 36)
print(f"Quantidade de valores somados: {quantidade}")
print(f"Soma atual: {soma}")
print(f"Média dos valores: {média:.2f}")