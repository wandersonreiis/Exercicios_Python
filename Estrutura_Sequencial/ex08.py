#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

vhora = float(input('Quanto você ganha por hora ? '))
htrabmes = int(input('Quantas horas trabalhadas no mês? '))

salario = vhora * htrabmes

print('O seu salário no mês atual é: ', salario)