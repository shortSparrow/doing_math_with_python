import math

def variance(arr):
  total = sum(arr)
  mean = total/len(arr)

  total_sum = 0
  for item in arr:
    diff = item - mean
    total_sum += diff*diff
  
  return total_sum/len(arr)

def standard_deviation(variance):
  return math.sqrt(variance)

variance_result = variance([60, 70, 100, 100, 200, 500, 500, 503, 600,  900, 1000, 1200])

# print(variance_result) # 141047.35416666666
# print(standard_deviation(variance_result)) # 375.5627166887931