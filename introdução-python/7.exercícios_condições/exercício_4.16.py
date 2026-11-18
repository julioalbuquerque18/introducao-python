print("-" * 5 + " EXERCÍCIO 4.16 " + "-" * 5)

média = int(input("Digite sua média: "))

if média < 4:
    print("Infelizmente você reprovou")
if média >= 4 and média < 7:
    print("Você ficou de recuperação")
if média >= 7:
    print("Você passou de ano")