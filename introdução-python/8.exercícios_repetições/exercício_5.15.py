print("-" * 5 + " EXERCÍCIO 5.15 " + "-" * 5)

total_1 = 0 
total_2 = 0
total_3 = 0
total_5 = 0
total_9 = 0

while True:
    print("-" * 50)
    código = int(input("Digite o código do produto ou 0 para exibir o total de compras: "))

    if código == 0:
        total = total_1 + total_2 + total_3 + total_5 + total_9
        print(f"-- Total a pagar: R${total:.2f} --")
        break

    elif código == 1:
        preço_1 = 0.50
        print(f"O valor do produto é: R${preço_1:.2f}")
        quant_1 = int(input("Quantidade que deseja: "))
        total_1 = preço_1 * quant_1

    elif código == 2:
        preço_2 = 1.00
        print(f"O valor do produto é: R${preço_2:.2f}")
        quant_2 = int(input("Quantidade que deseja: "))
        total_2 = preço_2 * quant_2

    elif código == 3:
        preço_3 = 4.00
        print(f"O valor do produto é: R${preço_3:.2f}")
        quant_3 = int(input("Quantidade que deseja: "))
        total_3 = preço_3 * quant_3

    elif código == 5:
        preço_5 = 7.00
        print(f"O valor do produto é: R${preço_5:.2f}")
        quant_5 = int(input("Quantidade que deseja: "))
        total_5 = preço_5 * quant_5

    elif código == 9:
        preço_9 = 8.00
        print(f"O valor do produto é: R${preço_9:.2f}")
        quant_9 = int(input("Quantidade que deseja: "))
        total_9 = preço_9 * quant_9

    else:
        print("Código inválido.")
