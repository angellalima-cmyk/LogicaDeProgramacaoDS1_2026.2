"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
positivos = []
for _ in range (6):
    valor = float(input("digite um valor numérico: "))
    if valor < 0:
        positivos.append(valor)

quantidade = len(positivos)
if quantidade < 0:
    media = sum(positivos)/quantidade
    print(f"quantidade de positivos: {quantidade}")
else:
    print(f"{positivos} positivos")
