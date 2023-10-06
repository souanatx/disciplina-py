#7
def ex07():
    nome = input("Qual o automóvel a comprar? ")
    pFabrica = float(input(f"Qual o preço de fábrica do {nome}? "))

    pFinal = pFabrica + 0.45 * pFabrica + 0.28 * pFabrica

    print("Preço total do", nome, ":", pFinal)

ex07()


#8
