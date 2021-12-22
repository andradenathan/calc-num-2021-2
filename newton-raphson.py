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

def newton_raphson(x, iteracoes_max):
  """
  Método de Newton-Raphson para encontrar raízes aproximadas
  """
  i = 0
  while i < iteracoes_max:
    x = x - (f(x) / derivada(x))
    i += 1
  
  return x