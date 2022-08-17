# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

n1 = input('digite um número: ')

if float(n1) >0:
    print(n1, ' é positivo')
elif float(n1) ==0:
    print(n1, ' é neutro')
else:
      print(n1, ' é negativo')