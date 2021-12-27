from math import fabs

def f(x):
  """
  Função definida para utilizarmos no cálculo de Newton-Raphson
  """
  return x**2 - 3*x + 1

def secante(x, x1, tolerancia, iteracao_max):
  """
  Método da Secante para encontrar raízes aproximadas
  """
  # Teste para saber se f(x) já é uma raíz aproximada.
  if fabs(f(x)) <= tolerancia:
    return x

  i = 0
  while i <= iteracao_max:
    x2 = (x * f(x1) - (x1 * f(x)))/(f(x1) - f(x))
    
    # Verifica a raíz para o novo ponto
    if fabs(f(x2)) <= tolerancia:
      return x2

    x, x1 = x1, x2

  raise ValueError("Número máx. de iterações atingido")