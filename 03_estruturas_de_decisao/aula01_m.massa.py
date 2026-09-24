# # TODO: Implemente a expressão de validação
# media_aluno = 7.5
# frequencia_percentual = 80

# # Crie a variável aprovado com a expressão lógica
# aprovado = None # Substitua None pela expressão lógica
# print("Status de aprovação:", aprovado)

# media = float(input("digite a media final: "))
# frequencia_percentual = float(input("digite frequencia porcentual: ")) 

# nota1 = 4.4
# nota2 = 8.7
# nota3 = 10.0

media = float(input("digite media: "))
frequencia_percentual = int(input("digite frequencia"))

aprovado = media >= 6 and frequencia_percentual >= 70
reprovado = media < 6 and frequencia_percentual < 70 
if aprovado:
    print("voce foi aprovado!")
else:
    print("Reprovado")
