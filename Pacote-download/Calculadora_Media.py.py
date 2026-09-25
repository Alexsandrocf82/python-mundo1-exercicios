#Criar um programa que receba duas notas de um aluno, calcule a média e informe se ele foi aprovado ou reprovado.
print('=' * 40)
print('CALCULADORA DE MÉDIA DE ALUNOS'.center(40))
print('=' * 40)
nome = input('Digite o nome do aluno: ')
nota1  = float(input('Digite a primeira nota: '))
nota2 = float (input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print('=' * 40)
print(f'Aluno: {nome}')
print(f'Média: {media:.2f}')

if media >=7:
    print('Situação:APROVADO')
else:
    print('Situação:REPROVADO')

print('=' * 40)