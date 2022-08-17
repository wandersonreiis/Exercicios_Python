# Faça um Programa que peça dois números e imprima o maior deles.
n1 = input('Digite um Número: ')

n2 = input('Digite outro Número: ')


if float(n1) > float(n2):
    print("O maior valor é:", n1)

elif float(n1) == float(n2):
        print("Os valores são iguais")

else:
        print("O maior valor é:", n2)