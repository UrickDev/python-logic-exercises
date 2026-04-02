import random

alunos = []
#Loop infinito
while True:
    #Input dos alunos
    print('Opções abaixo (responda com números): ')
    operacao = int(input('[1]-Adicionar aluno / [2]-Sortear\n:'))

    if operacao  == 1:
        alunos.append(input('Informe o nome do aluno: '))
    #Sortea e para o sistema
    elif operacao == 2:
        sorteado = (random.choice(alunos))
        print(f'O aluno sorteado foi: {sorteado}')
        break
    #Avisa erro
    else:
        print('Isso não é uma opção válida')

