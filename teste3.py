import json

# Carregar os dados do arquivo JSON
with open("dados.json", "r") as file:
    faturamento = json.load(file)

# Filtrar os dias com faturamento maior que 0
valores = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

# Calcular o menor e maior valor de faturamento
menor_valor = min(valores)
maior_valor = max(valores)

# Calcular a média mensal de faturamento
media_mensal = sum(valores) / len(valores)

# Contar os dias com faturamento superior à média mensal
dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
