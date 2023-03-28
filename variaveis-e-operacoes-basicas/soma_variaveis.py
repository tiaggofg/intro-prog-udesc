var_1 = input("Digite um valor: ")
var_2 = input("Digite outro valor: ")
var_3 = input("Digite mais um valor: ")

try:
    var_1 = int(var_1)
    var_2 = int(var_2)
    var_3 = int(var_3)
except ValueError:
    print("Um ou mais valores digitados são inválidos. Encerrando a execução do programa...")
    exit

soma = var_1 + var_2 + var_3

print(f"\nA soma dos valores digitados é {soma}")