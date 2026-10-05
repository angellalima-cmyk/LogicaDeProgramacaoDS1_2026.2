"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
2 - X-Salada: R$ 4.50
3 - X-Bacon: R$ 5.00
4 - Torrada Simples: R$ 2.00
5 - Refrigerante: R$ 1.50

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:

cardapio = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50,
}

codigo = int(input("digite o codigo do item (1 a 5): "))
quantidade = int(input("digite a quantidade consumida: "))

if codigo in cardapio:
    total = cardapio[codigo] * quantidade
    print(f"Total para pagar: R$ {total:.2f}")
else:
    print("Código de item inválido.")
