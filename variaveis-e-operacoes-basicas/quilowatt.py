"""
Sabe-se que o quilowatt de energia custa um quinto do salário mínimo. Escreva um programa que receba
o valor do salário mínimo e a quantidade de quilowatts consumida por uma residência. Calcule e mostre:

a) o valor de cada quilowatt;
b) o valor da conta de energia elétrica dessa residência;
c) o valor a ser pago com desconto de 15%.
"""

print('Digite o valor do salário mínimo e a quantidade de energia consumida em quilowatts')

salario_minimo = float(input('Salário mínimo: '))
quillowatts = float(input('Energia consumida em KW: '))

custo_killowatt = salario_minimo / 5
custo_energia = custo_killowatt * quillowatts
custo_energia_com_desconto = custo_energia - (custo_energia * 15/100)

print(f'\nO valor do Kilowatt é $ {custo_killowatt}')
print(f'O valor da conta de energia é $ {custo_energia}')
print(f'O valor da conta de energia com 15% de desconto é $ {custo_energia_com_desconto}')