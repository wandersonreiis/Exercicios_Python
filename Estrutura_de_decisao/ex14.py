# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E



n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))
while n1 >10 or n2>10 :
    print('O Valor Max da nota é 10:')
    n1 = float(input('Digite uma nota: '))
    n2 = float(input('Digite outra nota: '))

media = (n1+n2) / 2

if media < 4:
    conceito = 'E'
    print('Sua média é: ', media, ' e seu conceito é : ', conceito)

elif media >=4 and media <6 :
    conceito = 'D'
    print('Sua média é: ', media, ' e seu conceito é : ', conceito)

elif media >=6 and media <7.5 :
    conceito = 'C'
    print('Sua média é: ', media, ' e seu conceito é : ', conceito)

elif media >=7.5 and media <9 :
    conceito = 'B'
    print('Sua média é: ', media, ' e seu conceito é : ', conceito)

else:
    conceito = 'A'
    print('Sua média é: ', media, ' e seu conceito é : ', conceito)