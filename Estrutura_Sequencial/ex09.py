# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

tempfahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
tempcel = 5 * ((tempfahrenheit-32) / 9)

print('A temperatura atual é: ', tempcel,'°C')
