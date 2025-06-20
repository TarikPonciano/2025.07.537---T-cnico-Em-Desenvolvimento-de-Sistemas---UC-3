#Calcule os encargos de um funcionário com base na sua carga horária e valor da hora trabalhada. Imprima de maneira formatada.


print("Sistema RH XYZ")

cargaHoraria = int(input("Digite a carga horária do funcionário em horas:"))
valorHora =  float(input("Digite o valor hora do funcionário em reais: R$ "))

resultado = cargaHoraria * valorHora
print(f"O valor total a ser pago ao funcionário é de R$ {resultado:.2f}")