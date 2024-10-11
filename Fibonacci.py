def fibonacci(n):
  """
  Verifica se um número pertence à sequência de Fibonacci.

  Args:
    n: O número a ser verificado.

  Returns:
    Uma string informando se o número pertence ou não à sequência.
  """
  a = 0
  b = 1
  while a <= n:
    if a == n:
      return f"O número {n} pertence à sequência de Fibonacci."
    a, b = b, a + b
  return f"O número {n} não pertence à sequência de Fibonacci."

# Entrada do usuário
numero = int(input("Digite um número: "))

# Chamada da função e impressão do resultado
print(fibonacci(numero))