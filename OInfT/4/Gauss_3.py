import numpy as np
import math as ma
import matplotlib.pyplot as plt

_F = lambda x: x * ma.log(x) + ma.sin(2 * x) * 5 / 4 - 7 * x / 2
_f = lambda x: ma.log(x) - 5 * (ma.sin(x) ** 2)
_f_1 = lambda x: 1 / x - 10 * (ma.sin(x) * ma.cos(x))
_f_2 = lambda x: -(1 / (x ** 2) + 10 * ((ma.cos(x) ** 2) - (ma.sin(x) ** 2)))


_a, _b = 3, 6
I_fx_dx = (_F(_b) - _F(_a))

_h = [0.2, 0.1, 0.05, 0.01, 0.005]


def derive_f_1(f, x, h):
  return (f(x + h) - f(x - h)) / (2 * h)

def derive_f_2(f, x, h):
  return (f(x - h) - 2 * f(x) + f(x + h)) / (h**2)

def integrate(f, x_points, h):
  I = 0

  for x_i in x_points:
    x_i_0 = x_i
    x_i_1 = x_i + h * ma.sqrt(15) / 5
    x_i_2 = x_i - h * ma.sqrt(15) / 5

    I += 5/18 * _f(x_i_1) + 4/9 * _f(x_i_0) + 5/18 * _f(x_i_2)

  return h * I


if __name__ == "__main__":
  x_points = list(np.arange(_a - 0.05, _b + 0.05, 0.05))

  F_points = [_F(x) for x in x_points]
  f_points = [_f(x) for x in x_points]
  f_1_points = [_f_1(x) for x in x_points]
  f_2_points = [_f_2(x) for x in x_points]

  plt.figure()

  plt.plot(x_points, F_points, label='Antiderivative')
  plt.plot(x_points, f_points, label='Function')
  plt.plot(x_points, f_1_points, label='Derivative')
  plt.plot(x_points, f_2_points, label='Second derivative')

  plt.legend()
  plt.figure()

  for h in _h:
    x_points = list(np.arange(_a, _b + h/2, h))

    I_approx = integrate(_f, x_points, h)
    I = _F(x_points[-1]) - _F(x_points[0])
    err = abs(I_approx - I)

    print('----')
    print('h={}'.format(h))
    print('I_approx={}'.format(I_approx))
    print('I={}'.format(I))
    print('err={}'.format(err))

    f_1_approx_errors = [abs(_f_1(x) - derive_f_1(_f, x, h)) for x in x_points]
    f_2_approx_errors = [abs(_f_2(x) - derive_f_2(_f, x, h)) for x in x_points]

    plt.plot(x_points, f_1_approx_errors, label='Approximate derivative, h={}'.format(h))
    plt.plot(x_points, f_2_approx_errors, label='Approximate second derivative, h={}'.format(h))

    pass

  plt.legend()
  plt.show()

  print()

  pass
