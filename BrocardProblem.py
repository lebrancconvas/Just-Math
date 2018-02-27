import math
def brocard_problem():
  num = int(input("N = "))
  n = math.factorial(num)
  msq = n + 1
  m = math.sqrt(msq)
  return m
  
print(brocard_problem())