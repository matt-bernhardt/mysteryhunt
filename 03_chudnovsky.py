# Calculating the area of the circular field...
def func(maxK, prec, disp):
  gc().prec = prec
  M, L, X, S = 1, 13591409, 1, 13591409
  for k in range(1, maxK):
    K = 6 + 12*k    
    M = (K**3 - 16*K) * M // (k+1)**3
    L += 545140134
    X *= -262537412640768000
    S += Dec(M * L) / X
  pi = 426880 * Dec(10005).sqrt() / S
  pi = Dec(str(pi)[:disp])
  return pi
