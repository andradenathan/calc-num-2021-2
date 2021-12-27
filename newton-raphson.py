from math import fabs

def f(x):
  """
  Função definida para utilizarmos no cálculo de Newton-Raphson
  """
  return x**2 - 3*x + 1

def derivada(x):
  """
  Derivada da função f(x) = x² - 3x + 1
  """
  return 2*x - 3

def newton_raphson(x, tolerancia, iteracao_max):
  """
  Método de Newton Raphson para encontrar raízes aproximadas
  """
  # Caso já seja encontrado a raíz de primeira para x, retorne-a diretamente.
  if fabs(f(x)) <= tolerancia:
    return x

  i = 0
  # Queremos que o nosso critério ao invés da diferença entre os pontos serem 
  # menor do que o erro, tomaremos a iteração máxima como a nossa 
  # forma de aproximação.
  while i <= iteracao_max:
    x1 = x - (f(x) / derivada(x))
    if fabs(f(x1)) <= tolerancia:
      return x1
    x = x1
    i += 1
  
  raise ValueError("Número máx. de iterações atingido")