import json

def analisar_faturamento(dados):
  """
  Calcula o menor, o maior valor de faturamento e o número de dias com 
  faturamento acima da média.

  Args:
    dados: Um dicionário contendo os dados de faturamento diário.

  Returns:
    Uma tupla contendo o menor valor, o maior valor e o número de dias 
    com faturamento acima da média.
  """
  valores = [v for v in dados.values() if v > 0]
  menor_valor = min(valores)
  maior_valor = max(valores)
  media_mensal = sum(valores) / len(valores)
  dias_acima_da_media = sum(1 for v in valores if v > media_mensal)
  return menor_valor, maior_valor, dias_acima_da_media

# Carregar os dados de faturamento de um arquivo JSON (exemplo)
with open('faturamento.json', 'r') as f:
  faturamento_mensal = json.load(f)

# Chamada da função e impressão dos resultados
menor, maior, dias_acima = analisar_faturamento(faturamento_mensal)
print(f"Menor valor de faturamento: R$ {menor:.2f}")
print(f"Maior valor de faturamento: R$ {maior:.2f}")
print(f"Dias com faturamento acima da média mensal: {dias_acima}")