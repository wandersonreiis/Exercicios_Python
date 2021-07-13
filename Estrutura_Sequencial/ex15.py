''''15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    1. salário bruto.

    2. quanto pagou ao INSS.

    3. quanto pagou ao sindicato.

    4. o salário líquido.

    5. calcule os descontos e o salário líquido, conforme a tabela abaixo:

    

       ```
       + Salário Bruto : R$
       - IR (11%) : R$
       - INSS (8%) : R$
       - Sindicato ( 5%) : R$
       = Salário Liquido : R$
       ```

       

       Obs.: Salário Bruto - Descontos = Salário Líquido.

'''
imp_renda = 0.11
inss = 0.08
sindicato = 0.05

'''DESCONTOS'''




sal_horas = float(input('Quanto você ganha por hora ? '))
hor_trab_mes = int(input('Quantas horas você trabalhou no mês? '))
sal_bruto = sal_horas * hor_trab_mes
d_imp_renda = sal_bruto * imp_renda
d_inss = sal_bruto * inss
d_sindicato = sal_bruto * sindicato
sal_liquido = sal_bruto - d_imp_renda - d_inss - d_sindicato




print('Seu salário Bruto é: ', sal_bruto)
print('Seu salário Liquido é: ', sal_liquido)
print('Você pagou ao INSS um total de:', d_inss)
print('Você pagou de Imposto de renda um total de: ', d_imp_renda)
print('Você pagou ao Sindicato um total de: ', d_sindicato)
