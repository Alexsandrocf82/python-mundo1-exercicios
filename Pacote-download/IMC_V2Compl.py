peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura **2)
peso_minimo = 18.5 * (altura **2)
peso_maximo = 25 * (altura **2)

# Classificação do IMC
if imc <18.5:
    classificacao = 'Abaixo do Peso'
elif imc < 25:
    classificacao = 'Peso Normal'
elif imc < 30:
    classificacao = 'Sobrepeso'
else:
    classificacao = 'Obesidade'

# Situação  em relação a faixa de peso

if peso < peso_minimo:
    situacao = 'Abaixo da Faixa'
    diferenca = peso_minimo - peso
elif peso < peso_maximo:
    situacao = 'Dentro da Faixa'
else:
    situacao = 'Acima da Faixa'
    diferenca = peso - peso_maximo

# Resultados
print('\n ========== RESULTADO ==========')
print(f'Seu peso é {peso:.2f} Kg')
print(f'Sua altura é {altura:.2f} m')
print(f'Seu IMC é {imc:.2f}')
print(f'Classificação: {classificacao}')

print(f'\n Faixa de Referência:')
print(f'Peso mínimo  para faixa: {peso_minimo:.2f}Kg')
print(f'Peso máximo para faixa: {peso_maximo:.2f}Kg')

print(f'Situação:{situacao}')

if situacao == 'Abaixo da Faixa':
    print(f'Faltam aproximadamente {diferenca:.2f} Kg para atingir o limite inferior da faixa de peso.')
elif situacao == 'Dentro da Faixa':
    print('Seu peso está dentro da Faixa de Referência')
else:
    if abs(diferenca) < 0.01:
        print('Seu peso está exatamente no limite superior da faixa de Referência.')
    else:
        print(f'Você está aproximadamente {diferenca:.2f} Kg acima do limite superior da faixa de peso.')
    #print(f' Você está aproximadamente {diferenca:.2f} Kg acima do limite superior da faixa de peso.')
'''elif situacao == 'Acima da Faixa':
     #if round(diferenca, 2) == 0:
        #print('Seu peso está exatamente no limite superior da faixa de peso')
     #else:
       # print(f' Você está aproximadamente {diferenca:.2f}Kg acima do limite superior da faixa de peso.')
else:
    print('Seu peso está dentro da faixa de Referência de peso.')'''

print('==================================')


     


                     
