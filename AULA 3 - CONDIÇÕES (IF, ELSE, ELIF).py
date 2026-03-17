while True:

    exercicio = int(input("Qual exercicio quer executar? "))

    if exercicio == 5:

        val1 = int(input("Primeiro valor da operação: "))
        val2 = int(input("Segundo valor da operação: "))
        op = input("Qual operação? + - x / ")

        soma = val1 + val2
        sub = val1 - val2
        mul = val1 * val2
        div = val1 / val2

        if op == "+":
            print("Seu resultado é:", soma)

        elif op == "-":
            print("Seu resultado é:", sub)

        elif op == "x":
            print("Seu resultado é:", mul)

        elif op == "/":
            print("Seu resultado é:", div)

    elif exercicio == 6:

        casa = float(input("Qual o valor da casa desejada? "))
        salario = float(input("Qual seu salário? "))
        anos = int(input("Quantos anos pretende pagar? "))

        parcelas = anos * 12
        valor_parcela = casa / parcelas

        if valor_parcela <= salario * 0.30:
            print("Seu financiamento foi aprovado")

        else:
            print("Sua renda é incompatível")

    else:
        print("Choose a valid exercise")

    print()
    input("Pressione ENTER para voltar ao menu...")
    print()
