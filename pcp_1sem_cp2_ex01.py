estado = int(input("Digite o código do estado de origem (1 a 5): "))
peso_cargaT = float(input("Digite a carga do caminhão em toneladas: "))
codigo_carga = int(input("Digite o código da carga (10 a 40): "))

peso_cargaKg = peso_cargaT * 1000

if 10 <= codigo_carga <= 20:
    preco_kg = 100
elif 21 <= codigo_carga <= 30:
    preco_kg = 250
else:
    31 <= codigo_carga <= 40
    preco_kg = 340

preco_carga = preco_kg * peso_cargaKg

if estado == 1:
    imposto = 0.35
elif estado == 2:
    imposto = 0.25
elif estado == 3:
    imposto = 0.15
elif estado == 4:
    imposto = 0.05
else:
    imposto = 0

valor_imposto = imposto * preco_carga

valor_total = valor_imposto + preco_carga

print(f"Peso da carga em kg: {peso_cargaKg:.2f}")
print(f"Preço da carga: R$ {preco_carga:.2f}")
print(f"Valor do imposto: R$ {valor_imposto:.2f}")
print(f"Valor total: R$ {valor_total:.2f}")
