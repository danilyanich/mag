import numpy as np
import math as ma
import matplotlib.pyplot as plt

_f = lambda x: ma.log(x) - 5 * ma.cos(x)
_a, _b = 1, 8
_m, _n = 4, 4


def __polynom_part(x, y, k):
  p = np.poly1d([1])

  for i in range(len(x)):
    if i == k:
      continue
    p_part = np.poly1d([1, -x[i]])
    p = p * p_part / (x[k] - x[i])

  return p * y[k]


def lagrange_polynom(x, y):
  lp = sum(__polynom_part(x, y, k) for k in range(len(x)))
  return lp


if __name__ == "__main__":
  points = [_a + i * (_b - _a) / (_m - 1) for i in range(_m)]
  values = [_f(x) for x in points]

  lp = lagrange_polynom(points, values)

  x_points = list(np.arange(_a, _b + 0.1, 0.1))
  lp_points = [lp(x) for x in x_points]
  f_points = [_f(x) for x in x_points]

  plt.plot(points, values, 'ro')
  plt.plot(x_points, lp_points, label='Lagrange')
  plt.plot(x_points, f_points, label='Function')
  plt.legend()
  plt.show()

  pass
