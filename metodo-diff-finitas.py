import numpy as np

# Utilizaremos a seguinte função: x/4y' - 2y + 12x - 3

def p(x):
  """
  Definição da função p(x) que acompanha a derivada de 1ª ordem
  """
  return x/4

def q(x):
  """
  Constante q(x) que acompanha o termo y
  """
  return -2

def r(x):
  """
  Termo independente que não acompanha o y
  """
  return 12*x - 3

def metodo_dif_finitas(x, y, xf, yf, N):
  delta_x = (y - x)/N
  lista_x = np.linspace(x + delta_x, xf - delta_x, N-1)
  dimensao = coluna = linha = N - 1

  matrizA = np.zeros((coluna, linha))
  vetorB = np.zeros(dimensao)

  for i in range(dimensao):
    aux = lista_x[i]
    for j in range(dimensao):
      if i == j:
        matrizA[i][j] = 2 + q(x) * (delta_x ** 2)

      elif i == (j+1):
        matrizA[i][j] = -1 - p(x) * (delta_x/2)  
        
      elif i == (j-1):
        matrizA[i][j] = -1 + p(x) * (delta_x/2)

      else:
        matrizA[i][j] = 0

  for i in range(dimensao):
    aux = lista_x[i]
    if i == 0:
      vetorB[i] = 1 + p(x) * (delta_x/2) * y - r(x) * (delta_x ** 2)
    elif i == dimensao - 1:
      vetorB[i] = 1 - p(x) * (delta_x/2) * y - r(x) * (delta_x ** 2)
    else:
      vetorB[i] = - r(x) * (delta_x ** 2)

  solucao = np.linalg.solve(matrizA, vetorB)

  xj = [lista_x[i] for i in range(len(solucao))]
  yj = [solucao[i] for i in range(len(solucao))] 

  return xj, yj


metodo_dif_finitas(0, -1, 1, 0, 7)