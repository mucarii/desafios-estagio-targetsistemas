def inverter_string(s):
    resultado = ""
    for char in s:
        resultado = char + resultado
    return resultado

# Exemplo de uso
texto = "Teste tecnico estagio"
print(inverter_string(texto))
