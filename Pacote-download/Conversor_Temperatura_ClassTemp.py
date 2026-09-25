print ('=' * 40)
print('CONVERSOR DE TEMPERATURA'.center(40))
print('=' * 40)

celsius = float(input('Digite a temperatura em Celsius: '))

fahrenheit = celsius * 9 / 5+32
kelvin = celsius + 273.15

print()
print(f'Temperatura em Celsius: {celsius:.2f}°C')
print(f'Temperatura em Fahrenheit: {fahrenheit:.2f}°F')
print(f'Temperatura em Kelvin: {kelvin:.2f} K')

if celsius < 15 :
   classificacao = 'Frio'
elif celsius <= 25:
   classificacao = 'Agradável'
else:
   classificacao = 'Quente'
print(f'Classificação: {classificacao}')
