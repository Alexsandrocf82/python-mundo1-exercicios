'''' Crie um programa em Python que funcione como um Sistema de Classificação de Aluno
O programa deverá solicitar ao usuário as informações necessárias, calcular a média do aluno e informar sua situação final.'''
print('=' * 40)
print('SISTEMA DE CLASSIFICAÇÃO DE ALUNO'.center(40))
print('=' * 40)

nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    situacao = 'REPROVADO'
elif media < 7:
    situacao = 'RECUPERAÇÃO'
else:
    situacao = 'APROVADO'
print()
print('=' * 40)
print('RESULTADO FINAL'.center(40))
print('=' * 40)

print(f'Aluno: {nome}')
print(f'Primeira nota: {nota1}')
print(f'Segunda nota: {nota2}')
print(f'Média: {media:.2f}')
print(f'Situação Final: {situacao}')
