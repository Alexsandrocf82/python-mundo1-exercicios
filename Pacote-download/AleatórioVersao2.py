#Criar um programa em Python no qual o computador escolha um número e o usuário tente adivinhar.

#O programa deverá:

#1.Gerar um número aleatório entre 1 e 10.
#2.Pedir ao usuário que faça um palpite.
#3.Comparar o palpite com o número secreto.
#4.Informar se o usuário:
#acertou;
#errou para cima;
#errou para baixo.
#Mostrar o número secreto ao final.

import random
print('='*40)
print('JOGO DE ADIVINHAÇÃO'.center(40))
print('='*40)

numero_secreto = random.randint(1, 10 )

print('\nVocê tem 2 chances para acertar!')

palpite = int(input('\n 1ª tentativa - Digite seu palpite: '))

if palpite == numero_secreto:

   print('\n VOCÊ ACERTOU!')

else:
    print('\nVocê não acertou. Vamos para a segunda chance ')

    if palpite > numero_secreto:

        print('DICA: O número secreto   é MENOR que o seu palpite.')

    else:

        print('DICA: O numero secreto é MAIOR que o seu palpite.')

    palpite = int(input('\n2ª tentativa - Digite seu palpite: '))

    if palpite == numero_secreto:
      print('\n VOCÊ ACERTOU!')
    else:
      print('\n VOCÊ ERROU')
      print(f' O numero secreto era:{numero_secreto}')
