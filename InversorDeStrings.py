def inverter_string(texto):
  """
  Inverte os caracteres de uma string.

  Args:
    texto: A string a ser invertida.

  Returns:
    A string invertida.
  """
  return texto[::-1]

# Entrada do usuário
string = input("Digite uma string: ")

# Chamada da função e impressão do resultado
string_invertida = inverter_string(string)
print(f"String invertida: {string_invertida}")