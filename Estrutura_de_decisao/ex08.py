# Faça um programa que pergunte o preço de três produtos e 
# informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = float(input('Digite o Valor do Produto A: '))
p2 = float(input('Digite o Valor do Produto B: '))
p3 = float(input('Digite o Valor do Produto C: '))



if p1 > p2 and p1 > p3 :
    print("Você deve compar o produto: A")
elif p2 > p3:
     print("Você deve compar o produto: B")
else:
     print("Você deve compar o produto: c")


