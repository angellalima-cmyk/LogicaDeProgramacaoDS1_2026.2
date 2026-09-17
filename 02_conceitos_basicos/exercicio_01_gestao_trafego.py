"""
EXERCÍCIO 01: Gestão de Tráfego Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
A loja Casas Paulino está veiculando anúncios no Meta Ads em Tianguá.
Escreva um programa que leia:
1. O valor total investido na campanha (em R$).
2. O número total de cliques obtidos.

Calcule e mostre na tela o Custo Por Clique (CPC) médio da campanha formatado em reais.
"""

# TODO: Desenvolva o algoritmo abaixo:
valor_total = float(input("digite o valor total investido na campanha: "))
total_cliques = float(input("digite o numero total de cliques: "))
CPC = valor_total/total_cliques
print(f"qual o valor medio de cada cliques é R$ {CPC: .2f}")
