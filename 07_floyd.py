# Seeing if the beanstalk has any loops in it...
def func(f, start):
  if start == f(start):
    return 0, 0       
  tortoise = f(start)
  hare = f(tortoise)
  while tortoise != hare:
    tortoise = f(tortoise)
    hare = f(f(hare))
  cycle_start = 0
  tortoise = start
  while tortoise != hare:
    tortoise = f(tortoise)
    hare = f(hare)
    cycle_start += 1
  cycle_length = 1
  hare = f(tortoise)
  while tortoise != hare:
    hare = f(hare)
    cycle_length += 1
  return cycle_length, cycle_start
