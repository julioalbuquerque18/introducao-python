while True:
    print("-" * 50)
    print("Menu das Operações:\n 0 - Sair\n 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão")
    operacao = int(input("Digite a operação que deseja: "))
    print("-" * 50)

    if operacao == 0:
        break

    elif operacao == 1:
        i = int(input("Digite um valor para a tabuada: "))
        for j in range(1, 11):
            print(f"{i} + {j} = {i + j}")

    elif operacao == 2:
        i = int(input("Digite um valor para a tabuada: "))
        for j in range(1, 11):
            print(f"{i} - {j} = {i - j}")

    elif operacao == 3:
        i = int(input("Digite um valor para a tabuada: "))
        for j in range(1, 11):
            print(f"{i} * {j} = {i * j}")

    elif operacao == 4:
        i = int(input("Digite um valor para a tabuada: "))
        for j in range(1, 11):
            print(f"{i} / {j} = {i / j:.2f}")

    else:
        print("Operação Inválida.")