"""
EXERCÍCIO 05: Acesso à Bilheteria do Parque
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba a idade do visitante (valor base do ingresso: R$ 100,00):
- Menor que 12 anos: "Infantil" (50% de desconto -> R$ 50,00)
- Maior ou igual a 60 anos: "Melhor Idade" (Gratuidade -> R$ 0,00)
- Demais idades: "Integral" (R$ 100,00)

Imprima o tipo de bilhete e o valor final a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:

idade = int(input("digite a idade do visitante:"))
valor_base = 100.00

if idade < 12:
    tipo_bilhete = "infantil"
    valor_final = valor_base * 0.50
elif idade >= 60:
    tipo_bilhete = "melhor idade"
    valor_final = 0.00
else:
    tipo_bilhete = "integral"
    valor_final = valor_base

    print(f"tipo de bilhete: {tipo_bilhete}")
    print(f"valor final a pagar: R$ {valor_final:.2f}")
