import numpy as np
import math as ma
import matplotlib.pyplot as plt


_f = lambda x: ma.exp(x) / (x ** 3) - 30 * ma.cos(x)


_a, _b = 0.2, 12


def find_min(F, a, b, eps):
  x_1 = a
  x_2 = (b + a) / 2
  x_3 = b

  y_1 = F(x_1)
  y_2 = F(x_2)
  y_3 = F(x_3)

  if not (y_1 - 2 * y_2 + y_3) > 0:
    raise 'Function is not convex inside [{}, {}]'.format(a, b)

  zm = 2*eps

  it = 0

  while abs(zm) > eps:
    z_1 = x_1 - x_3
    z_2 = x_2 - x_3

    p = ((y_1 - y_3) * z_2 - (y_2 - y_3) * z_1) / (z_1 * z_2 * (z_1 - z_2))
    q = ((y_1 - y_3) * (z_2**2) - (y_2 - y_3) * (z_1**2)) / (z_1 * z_2 * (z_2 - z_1))
    zm = -q / (2 * p)

    x_1 = x_2
    x_2 = x_3
    x_3 = x_3 + zm

    y_1 = y_2
    y_2 = y_3
    y_3 = F(x_3)

    it += 1
    pass

  return x_3, it


if __name__ == "__main__":
  x_points = list(np.arange(_a - 0.05, _b + 0.05, 0.05))

  f_points = [_f(x) for x in x_points]

  eps = 10e-5

  x_min_1, _ = find_min(_f, 0.5, 2, eps)
  x_min_2, _ = find_min(_f, 4, 8, eps)
  x_min_3, _ = find_min(_f, 10, 12, eps)

  x_min = [x_min_1, x_min_2, x_min_3]
  f_min_x = [_f(x) for x in x_min]

  plt.figure()
  plt.plot(x_min, f_min_x, 'ro')
  plt.plot(x_points, f_points, label='Function')
  plt.legend()

  plt.figure()

  epss = [10e-2, 10e-3, 10e-4, 10e-5, 10e-6]

  for eps in epss:
    _, it = find_min(_f, 4, 8, eps)
    plt.plot(eps, it, 'ro')
    pass

  plt.show()
  pass
