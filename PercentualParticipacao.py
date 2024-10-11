def calcular_percentuais(faturamento):
  """
  Calcula o percentual de representação de cada estado no faturamento total.

  Args:
    faturamento: Um dicionário contendo o faturamento por estado.

  Returns:
    Um dicionário contendo o percentual de representação de cada estado.
  """
  total = sum(faturamento.values())
  percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}
  return percentuais

# Faturamento mensal por estado
faturamento_mensal = {
  "SP": 67836.43,
  "RJ": 36678.66,
  "MG": 29229.88,
  "ES": 27165.48,
  "Outros": 19849.53
}

# Chamada da função e impressão dos resultados
percentuais = calcular_percentuais(faturamento_mensal)
for estado, percentual in percentuais.items():
  print(f"{estado}: {percentual:.2f}%")