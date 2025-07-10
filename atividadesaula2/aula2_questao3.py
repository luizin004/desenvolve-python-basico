v1 = 10
v2 = 20

# Variável auxiliar
aux = v1
v1 = v2
v2 = aux

print(v1)  # Deve imprimir 20
print(v2)  # Deve imprimir 10
