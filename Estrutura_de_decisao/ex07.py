# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = input("Digite o primeiro número: ")
n2 = input("Digite o segundo número: ")
n3 = input("Digite o terceiro número:  ")


if float(n1)> float(n2) and float(n1) > float(n3) and float(n2)>= float(n3) :
    print('O Maior valor é: ',n1 , 'O menor Valor é: ', n3)

elif float(n1)> float(n2) and float(n1) > float(n3) and float(n3)>= float(n2) :
    print('O Maior valor é: ',n1 , 'O menor Valor é: ', n2)

elif float(n2)> float(n3) and float(n3)>= float(n1):
    print('O Maior valor é: ',n2 , 'O menor Valor é: ', n1)

elif float(n2)> float(n3) and float(n1)>= float(n3):
    print('O Maior valor é: ',n2 , 'O menor Valor é: ', n3)

elif float(n3)> float(n2) and float(n2)>= float(n1):
    print('O Maior valor é: ',n3 , 'O menor Valor é: ', n1)

elif float(n3)> float(n2) and float(n1)>= float(n2):
    print('O Maior valor é: ',n3 , 'O menor Valor é: ', n2)

elif float(n1) == float(n2) and float(n3) > float(n2) or float(n1) == float(n3) and float(n3) > float(n2):
       print('O Maior valor é: ',n3 , 'O menor Valor é: ', n2)

elif float(n1) == float(n2) and float(n2) > float(n3) or float(n1) == float(n3) and float(n2) > float(n3):
       print('O Maior valor é: ',n3 , 'O menor Valor é: ', n1)

elif float(n3) == float(n2) and float(n3) > float(n1) or float(n3) == float(n1) and float(n3) > float(n1):
       print('O Maior valor é: ',n3 , 'O menor Valor é: ', n1)

elif float(n3) == float(n2) and float(n1) > float(n3) or float(n3) == float(n3) and float(n1) > float(n3):
       print('O Maior valor é: ',n1 , 'O menor Valor é: ', n3)
              
else:
    print('Todos os valores são iguais')