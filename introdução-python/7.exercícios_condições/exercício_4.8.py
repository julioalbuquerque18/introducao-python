print("-" * 5 + " EXERCÍCIO 4.8 " + "-" * 5)
plano = input("Qual é o seu plano de celular? ")

if plano == "falopouco":
    minutos_no_plano = 100
    extra = 0.20
    preço = 50
if plano == "falomuito":
    minutos_no_plano = 500
    extra = 0.15
    preço = 99
else:
    print("Não conheço este plano.")

if plano == "falopouco" or plano == "falomuito":
    minutos_consumidos = int(input("Quantos minutos você consumiu? "))
    print(f"Você vai pagar: ")
    print(f"Preço do plano   R${preço:10.2f}")
    suplemento = 0
    if minutos_consumidos > minutos_no_plano:
        suplemento = extra * (minutos_consumidos - minutos_no_plano)
    print(f"Suplemento       R${suplemento:10.2f}")
    print(f"Total            R${preço + suplemento:10.2f}")