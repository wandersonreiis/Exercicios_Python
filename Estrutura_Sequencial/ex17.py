'''17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    

    - Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    - comprar apenas latas de 18 litros;
    - comprar apenas galões de 3,6 litros;
    - misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''


m_quadrado = int(input("Digite a quantidade de metros quadrados a serem pintados: "))
l_tinta = int(m_quadrado/6)

preco_lata = 80.0
preco_galao = 25
cap_lata = 18
cap_galao = 3.6

latas = int(l_tinta / cap_lata)
galoes = int(l_tinta / cap_galao)
total_lata = latas * preco_lata
total_galao = galoes * preco_galao

print('')