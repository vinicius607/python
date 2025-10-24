# n = int(input("Quantos alunos tem: "))
# lista_media = []

# for aluno in range(1, n+1):
#     print('Aluno', aluno)
#     prova1 = float(input("Nota da P1: "))
#     prova2 = float(input("Nota da P2: "))
#     media_aluno = (prova1 + prova2)/2
#     lista_media.append(media_aluno)
    
# contador = 1
# for media in lista_media:
#     print('Situação do Aluno', contador)
#     print('Media =', media)
#     if media >= 7:
#         print("Aprovado")
#     elif media >=4:
#         print('Prova Final')
#     else:
#         print('Reprovado')
#     contador = contador + 1


# contador = 0
# while contador < n:
#     media = lista_media[contador]
#     print('Situação do Aluno', contador+1)
#     print('Media =', media)
#     if media >= 7:
#         print("Aprovado")
#     elif media >=4:
#         print('Prova Final')
#     else:
#         print('Reprovado')
#     contador = contador + 1



# *******************************

# TUPLAS
# olhar o slide para ver os metodos

# lista_nomes = [
#     'Rafale','João',
#     'Maria','Luiza',
#     'Gabriel','Matheus'
# ]
# print(lista_nomes[0:4:2])
# print(lista_nomes[2:])
# print(lista_nomes[:5])


# tupla_nomes = [
#     'Rafale','João',
#     'Maria','Luiza',
#     'Gabriel','Matheus'
# ]

# print(tupla_nomes[0:4:2])
# print(tupla_nomes[2:])
# print(tupla_nomes[:5])

#exemplo4
#olha o slide

dicionario_cadastro = {
    'nome':'Rafael Mynssem',
    'endereco':'Marica',
    'idade':36,
    'cargo':'Professor Adjunto I',
    'Disciplina':'Algoritmo'
}
print(dicionario_cadastro)
# dicionario_cadastro['Disciplina'] = 'RPE2'
print(dicionario_cadastro['nome'])