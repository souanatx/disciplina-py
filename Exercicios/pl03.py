def somar():
    num1 = int(input("Insira um número: "))
    num2 = int(input("Insira outro número: "))

    # -- opção com cálculo antes de apresentação --
    # soma = num1 + num2
    # print(f"A soma é: {soma}")

    # -- opção com cálculo aquando da apresentação --
    print(f"A soma é: {num1 + num2}")


def subtrair():
    print("-- SUBTRAIR --")


def calculadora():
    op = 1
    while op > 0:
        print("Aplicação 1: Calculadora")
        print("1-Somar")
        print("2-Subtrair")
        print("0-Voltar ao menu anterior")
        op = int(input())

        if op == 0:
            break
        elif op == 1:
            somar()
        elif op == 2:
            subtrair()
        else:
            print("Opção inválida")


def lista_numeros():
    num1 = int(input("Insira o primeiro número: "))  # 4
    num2 = int(input("Insira o segundo número: "))  # 8
    # 4 5 6 7 8

    # opção com inversão de valores se num1>num2
    # if num1 > num2:
    #     temp = num1
    #     num1 = num2
    #     num2 = temp
    #
    # for x in range(num1, num2+1):
    #     print(x)

    # opção com inversão do ciclo se num1>num2
    if num1 < num2:
        for x in range(num1, num2 + 1, 1):  # 1 aumenta +1 a cada valor
            print(x)
    else:
        for x in range(num1, num2 - 1, -1):  # -1 retira +1 a cada valor
            print(x)


def menu():
    # print("Bem-vindo\nEscolha uma das seguintes opções:")
    op = 1
    while op > 0:
        print("Bem-vindo")
        print("Escolha uma das seguintes opções:")
        print("1-Calculadora")
        print("2-Lista de números")
        print("0-Sair")
        op = int(input())

        if op == 0:
            break
            # print("Sair")
        elif op == 1:
            calculadora()
        elif op == 2:
            lista_numeros()
        else:
            print("Opção inválida")


menu()
