# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia = int(input('Digite um numero de 1 a 7: '))
dia_semana={1:'domingo',2:'Segunda',3:'terça',4:'quarta',5:'quinta',6:'sexta',7:'sabado'}
for k,v in dia_semana.items():
    if dia == k:
     print(v)

   