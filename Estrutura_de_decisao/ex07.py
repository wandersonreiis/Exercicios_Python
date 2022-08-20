# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número:  "))


if n1> n2 and n1 > n3 and n2>= n3 :
    print('O Maior valor é: ',n1 , 'O menor Valor é: ', n3)

elif n1> n2 and n1 > n3 and n3>= n2 :
    print('O Maior valor é: ',n1 , 'O menor Valor é: ', n2)

elif n2> n3 and n3>= n1:
    print('O Maior valor é: ',n2 , 'O menor Valor é: ', n1)

elif n2> n3 and n1>= n3:
    print('O Maior valor é: ',n2 , 'O menor Valor é: ', n3)

elif n3> n2 and n2>= n1:
    print('O Maior valor é: ',n3 , 'O menor Valor é: ', n1)

elif n3> n2 and n1>= n2:
    print('O Maior valor é: ',n3 , 'O menor Valor é: ', n2)

elif n1 == n2 and n3 > n2 or n1 == n3 and n3 > n2:
       print('O Maior valor é: ',n3 , 'O menor Valor é: ', n2)

elif n1 == n2 and n2 > n3 or n1 == n3 and n2 > n3:
       print('O Maior valor é: ',n3 , 'O menor Valor é: ', n1)

elif n3 == n2 and n3 > n1 or n3 == n1 and n3 > n1:
       print('O Maior valor é: ',n3 , 'O menor Valor é: ', n1)

elif n3 == n2 and n1 > n3 or n3 == n3 and n1 > n3:
       print('O Maior valor é: ',n1 , 'O menor Valor é: ', n3)
              
else:
    print('Todos os valores são iguais')