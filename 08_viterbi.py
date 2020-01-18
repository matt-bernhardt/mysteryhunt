# Trying to determine the most likely thing the giant said...
def func(y, A, B, Pi):
  K = A.shape[0]
  T = len(y)
  T1 = np.empty((K, T), 'd')
  T2 = np.empty((K, T), 'B')
  T1[:, 0] = Pi * B[:, y[0]]
  T2[:, 0] = 0
  for i in range(1, T):
    T1[:, i] = np.max(T1[:, i - 1] * A.T * B[np.newaxis, :, y[i]].T, 1)
    T2[:, i] = np.argmax(T1[:, i - 1] * A.T, 1)
  x = np.empty(T, 'B')
  x[-1] = np.argmax(T1[:, T - 1])
  for i in reversed(range(1, T)):
    x[i - 1] = T2[x[0], i]
  return x, T1, T2
