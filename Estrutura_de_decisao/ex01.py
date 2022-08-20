# Faça um Programa que peça dois números e imprima o maior deles.
n1 = float(input('Digite um Número: '))

n2 = float(input('Digite outro Número: '))


if n1 > n2:
    print("O maior valor é:", n1)

elif n1 == n2:
        print("Os valores são iguais")

else:
        print("O maior valor é:", n2)