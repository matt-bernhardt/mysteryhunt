# Verifying the bean/cow transaction...
def func(account_no):
  num_digits = len(account_no)
  parity_check = num_digits ^ 2 
  print(parity_check)
  sum = 0
  for index in range(0, num_digits):
    digit = int(account_no[index])
    sum += digit
    if parity_check == (index % 2):
      sum += digit
      if (digit >= 5):
        sum -= 9
  return ( ( sum % 10) == 0)
