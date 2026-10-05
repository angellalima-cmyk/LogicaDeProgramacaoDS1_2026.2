"""
EXERCÍCIO 05: Feliz Nataaal!
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba um número inteiro I (nível de empolgação).
Utilize repetição para exibir a frase "Feliz natal!" repetindo a letra 'a'
da palavra natal exatamente I vezes (ex: I=5 -> "Feliz nataaaal!").
"""

# TODO: Desenvolva o algoritmo abaixo:
I = int(input("digite o nivel de empolgacao: "))
letras_a = "a" 

while True:
    if contador >= I:
        break

    for _ in range(1):
        letras_a += "a"

        print(f"feliz natal {letras_a}!" )