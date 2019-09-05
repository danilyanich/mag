import numpy as np
import math as ma

_d = -2
_q = -3.23

A = np.array([
  [_q, 1, 0, 0, 0],
  [1, -2, 1, 0, 0],
  [0, 1, -2, 1, 0],
  [0, 0, 1, -2, 1],
  [0, 0, 0, 1, _q],
])

b = np.array([0, _d, _d, _d, 0])


def square_root_method(A, b):
  n, m = A.shape

  d = np.empty(n)
  S = np.zeros((n, m))

  for k in range(n):
    _1 = A[k, k] - sum([d[i] * S[i, k]**2 for i in range(k)])
    d[k] = np.sign(_1)
    S[k, k] = ma.sqrt(ma.fabs(_1))

    for j in range(k+1, n):
      S[k, j] = (A[k, j] - sum([d[i]*S[i, k]*S[i, j] for i in range(k)])) / (S[k, k] * d[k])

  # inverse steps

  y = np.empty(n)
  x = np.empty(n)

  for i in range(n):
    y[i] = (b[i] - sum([d[k] * y[k] * S[k, i] for k in range(i)])) / (S[i, i] * d[i])

  for i in reversed(range(n)):
    x[i] = (y[i] - sum([S[i, k] * x[k] for k in range(i + 1, n)])) / S[i, i]

  return x


if __name__ == '__main__':
  x = square_root_method(A, b)

  print('x:', x)
  print('residual:', np.linalg.norm(b -A.dot(x)))
