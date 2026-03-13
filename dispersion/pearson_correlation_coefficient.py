def find_corr_x_y(x,y):
  n = len(x)
  # Find the sum of the products 
  prod = []
  for xi,yi in zip(x,y): 
      prod.append(xi*yi)
  sum_prod_x_y = sum(prod) 
  sum_x = sum(x)
  sum_y = sum(y)
  squared_sum_x = sum_x**2 
  squared_sum_y = sum_y**2    
  x_square = [] 
  for xi in x:
      x_square.append(xi**2)

  # Find the sum
  x_square_sum = sum(x_square)

  y_square=[]
  for yi in y:
      y_square.append(yi**2)

  # Find the sum
  y_square_sum = sum(y_square)

  # Use formula to calculate correlation
  numerator = n*sum_prod_x_y - sum_x*sum_y
  denominator_term1 = n*x_square_sum - squared_sum_x 
  denominator_term2 = n*y_square_sum - squared_sum_y
  denominator = (denominator_term1*denominator_term2)**0.5
  correlation = numerator/denominator
  
  return correlation


# print(find_corr_x_y([1,2,3,4,5], [2,4,6,8,10])) # 1.0
# print(find_corr_x_y([1,2,3,4,5], [3,6,9,12,15])) # 1.0
# print(find_corr_x_y([3,6,9,12,15], [1,2,3,4,5])) # 1.0
# print(find_corr_x_y([1,2,3,4,5], [-3,-6,-9,-12,-15])) # -1.0


# print(find_corr_x_y([1,2,3,4,5], [1,4,6,8,10])) # 0.9958932064677039
