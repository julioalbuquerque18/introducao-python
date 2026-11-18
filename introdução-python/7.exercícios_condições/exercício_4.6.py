print("-" * 5 + " EXERCÍCIO 4.6 " + "-" * 5)
distancia = int(input("Digite a distância que você vai percorrer em Km: "))

if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45

print(f"O valor da passagem para {distancia}Km é R${preço:1.2f}")