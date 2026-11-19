print("-" * 5 + " EXERCÍCIO 5.11 " + "-" * 5)
'''
x = 1
soma = 0

while x <= 5:
    n = int(input(f"{x} - Digite um número: "))
    soma = soma + n
    x = x + 1
print(f"Média dos números: {soma / 5:5.2f}")
'''

deposito = float(input("Depósito inicial: "))
juros = float(input("Taxa de juros (% ao mês): "))

saldo = deposito
mes = 1

while mes <= 24:
    juros_mes = saldo * (juros / 100)
    saldo = saldo + juros_mes
    print(f"{mes}° mês | Saldo = R${saldo:.2f}")
    mes = mes + 1

print("-" * 35)

total_juros = saldo - deposito
print(f"Total ganho com juros: R${total_juros:.2f}")