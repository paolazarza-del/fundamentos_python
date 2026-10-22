
# Ejemplo mínimo
linea = "    2026-10-12|ERROR|payment_gateway|Timeout en la respuesta  "

campos = [campo.strip() for campo in linea.split("|")]

print(campos)

print(campos[1])  # Resultado: ERROR

print(len(campos))  # Resultado: 4
