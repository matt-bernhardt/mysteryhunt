# Determining which contiguous section of land produced the most wheat...
def func(array):
  best_so_far = 0
  running_sum = 0
  for i in array:
    running_sum += i
    if running_sum > best_so_far:
      best_so_far = running_sum
    if running_sum < 0:
      running_sum = i 
  return best_so_far
