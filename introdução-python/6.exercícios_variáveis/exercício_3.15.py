print("-" * 5 + " EXERCÍCIO 3.15 " + "-" * 5)
anos_fumando = int(input("Quantidade de anos como fumante: "))
cig_diarios = int(input("Quantidade de cigarros diários: "))

dias_em_anos = anos_fumando * 365
total_cigarros = cig_diarios * dias_em_anos

min_perdidos = total_cigarros * 10
horas_perdidas = min_perdidos / 60
dias_perdidos = round(horas_perdidas / 24)
print(f"Dias perdidos devido ao fumo: {dias_perdidos}")