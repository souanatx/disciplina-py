# 1. Crie um algoritmo que lê o nome de uma pessoa e escreve “Olá” seguido do nome da pessoa.
def ex01():
    nome = input("Qual o seu nome? ")
    print("Olá", nome)


# 2. Crie um algoritmo que após ler dois números inteiros apresenta a sua soma.
def ex02():
    n1 = int(input("Insira o primeiro número: "))
    n2 = int(input("Insira o segundo número: "))

    # OPÇÃO A: GUARDA RESULTADO EM VARIÁVEL E APRESENTA
    soma = n1 + n2
    print("Soma:", soma)

    # OPÇÃO B: APRESENTA RESULTADO SEM GUARDAR EM VARIÁVEL
    print("Soma:", n1 + n2)


# 3. Crie um algoritmo que após ler dois números inteiros apresenta a sua diferença.
def ex03():
    n1 = int(input("Insira o primeiro número: "))
    n2 = int(input("Insira o segundo número: "))

    # OPÇÃO B: APRESENTA RESULTADO SEM GUARDAR EM VARIÁVEL
    print("Diferença:", n1 - n2)


# 4. Pretende-se lendo a base e altura de um triângulo calcular a sua área.
def ex04():
    base = float(input("Qual a base do triângulo? "))
    altura = float(input("Qual a altura do triângulo? "))
    area = base * altura / 2

    print("Área do triângulo:", area)


# 5. Faça um programa que receba um valor que é o valor pago, um segundo valor
# que é o preço do produto e retorne o troco a ser dado.
def ex05():
    preco = float(input("Qual o preço do produto? "))
    vPago = float(input("Quanto pagou pelo produto? "))
    troco = vPago - preco

    if troco >= 0:
        print("Troco: ", troco)
    else:
        print("Ainda falta pagar: ", troco * -1)


# 6. Faça um programa que receba o valor do quilo de um produto e a
# quantidade de quilos do produto consumida calculando o valor final a ser pago.
def ex06():
    pKg = float(input("Qual o preço de 1kg? "))
    quant = float(input("Qual a quantidade comprada? "))

    print("Valor a pagar: ", pKg * quant)


# 7. O preço de um automóvel é calculado pela soma do preço de fábrica com o preço dos
# impostos (45% do preço de fábrica) e a percentagem do revendedor (28% do preço de
# fábrica). Faça um algoritmo que leia o nome do automóvel e o preço de fábrica e
# escreva o nome do automóvel e o preço final.
def ex07():
    percImpostos = 0.45
    percRevendedor = 0.28
    nome = input("Qual o automóvel a comprar? ")
    pFabrica = float(input(f"Qual o preço de fábrica do {nome} "))

    pFinal = pFabrica + percImpostos * pFabrica + percRevendedor * pFabrica

    print("Preço total do", nome, ":", pFinal)


ex07()
