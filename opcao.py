from Funcoes import *
from menu import menu


opcao = 0
while opcao != 12:
    menu()
    opcao = int(input(' Escolhar uma opção :  '))

    if opcao == 1:
        matricula = int(input("Digite a matricula: "))
        nome = input("Digite seu nome: ")
        situacao=(False)
        matricular(matricula,nome,situacao,situacao,situacao)
    elif opcao == 2:
        listar_aluno()
    elif opcao == 3:
        listar_aluno_aprovado()
    elif opcao == 4:
        listar_aluno_recuperacao()
    elif opcao == 5:
        listar_aluno_reprovado()
    elif opcao == 6:
        nome = input("Digite um nome do aluno: ")
        buscar_por_nome(nome)
    elif opcao == 7:
        matricula = int(input('Digite a matricula: '))
        buscar_por_matricula(matricula)
    elif opcao == 8:
        matricula=int(input('Digite a matricula: '))
        excluir_aluno(matricula)
    elif opcao == 9:
        matricula = int(input('matricula: '))
        nota1 = float(input("digite a primeira nota: "))
        nota2 = float(input("digite a segunda nota: "))
        media = (nota1 + nota2) / 2
        Lancar_notas(matricula,nota1,nota2,media)
    elif opcao == 10:
        listar_notas()
    elif opcao == 11:
        matricula_aluno=int(input('Digite a matricula: '))
        excluir_notas(matricula_aluno)
    elif opcao == 12:
        exit()