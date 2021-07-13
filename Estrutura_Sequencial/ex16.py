'''
16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

m_quadrado = int(input("Digite a quantidade de metros quadrados a serem pintados: "))
l_tinta = int(m_quadrado/3)

precoL = 80.0
capacidadeL = 18

latas = int(l_tinta / capacidadeL)
total = latas * precoL


print('Para pintar sua parede vai ser necessário utilizar :', latas, 'Latas de tinta',)