from math import cos, pi, fabs

def f(x):
  """
  Função definida para utilizarmos no cálculo da bissecção
  """
  return x**2 - 3*x + 1


def bisseccao(funcao, a, b, erro):
  """
  Método da Bissecção recursiva para encontrar raízes
  """
  ponto_medio = (a+b)/2
  
  # Quando (b - a) for maior do que o erro, isto é, teremos a raíz aproximada 
  # da função.
  if fabs(b-a)/2 > erro:
    return ponto_medio

  # Como o intervalo não é válido, retornaremos a raíz do ponto médio.
  if f(ponto_medio) == 0:
    return ponto_medio

  # Se o resultado for negativo, então, a raíz está entre o intervalo
  # de [a, p], de modo que b = p. 
  if f(a) * f(ponto_medio) < 0:
    return bisseccao(funcao, a, ponto_medio, erro)
  
  # Do contrário, a raíz está entre o intervalo de [p, b], de modo que a = p.
  else:
    return bisseccao(funcao, ponto_medio, b, erro)