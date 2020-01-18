def func(n):
 g = lambda x: (x^2 + 1) % x
 x, y = 2, 2
 d = 1
 while d == 1:
   x = g(x)
   y = g(g(y))
   d = math.gcd(abs(x - y), n)
 if d != n:
   return d
 return -1
