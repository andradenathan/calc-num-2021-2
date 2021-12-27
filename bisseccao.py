from math import fabs

def f(x):
  """
  Função definida para utilizarmos no cálculo da bissecção
  """
  return x**2 - 3*x + 1


def bisseccao(f, a, b, tolerancia, iteracao_max):
  """
  Método da Bissecção recursiva para encontrar raízes
  """
  i = 0
  while i <= iteracao_max:
    p = (a+b)/2
    # Critério de parada, isto é, o intervalo não é válido, então retornaremos
    # a raíz do ponto médio.
    if fabs(b-a)/2 < tolerancia or f(p) == 0:
      return p

    # Se o resultado for negativo, então, a raíz está entre o intervalo
    # de [a, p], de modo que b = p. 
    if f(a) * f(p) < 0:
      b = p
  
    # Do contrário, a raíz está entre o intervalo de [p, b], de modo que a = p.
    else:
      a = p

    i += 1