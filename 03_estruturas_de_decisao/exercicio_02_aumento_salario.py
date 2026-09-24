"""
EXERCÍCIO 02: Aumento de Salário Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de um colaborador da escola e aplique o percentual de reajuste:
- 0.00 a 400.00: 15%
- 400.01 a 800.00: 12%
- 800.01 a 1200.00: 10%
- 1200.01 a 2000.00: 7%
- Acima de 2000.00: 4%

Imprima: novo salário, valor do reajuste ganho e percentual aplicado.
"""

# TODO: Desenvolva o algoritmo abaixo:

salario = float(input("digite o salario atual: R$ "))

if salario <= 400.00:
    reajuste = salario *0.15
    novo_salario = salario + reajuste
    print(f"seu novo salario e {novo_salario} ")
elif 400 < salario <= 800.00:
    reajuste = salario *0.12
    novo_salario = salario + reajuste
    print(f"seu novo salario e {novo_salario} ")
elif 800 < salario <= 1200.00:
    reajuste = salario * 0.10
    novo_salario = salario + reajuste
    print(f"seu novo salario e {novo_salario} ")
elif 1200 < salario <= 2000.00:
    reajuste = salario *0.7
    novo_salario = salario + reajuste
    print(f"seu noo salario e {novo_salario} ")
elif salario >= 2000.01:
    reajuste = salario *0.4
    novo_salario = salario + reajuste
    print(f"seu novo salario e {novo_salario} ")   
