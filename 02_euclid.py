# Planning the best way to divide up all these beans equally...
def func(a, b):
  if a < b:
    if (b % a) == 0:
      return b
    return func(b % a, a)
  else:
    if (a % b) == 0:  
      return b
    return func(a % b, b)
