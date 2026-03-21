import math
from sympy import FiniteSet

# Розрахунок періоду коливання маятника, який описується формулою T = 2*pi*sqrt(L/g)
# За звичних мов g=9.81, але якщо я хочу додати g не як константу, а як змінну, і припустимо 
# я хочу зробити розрахунок для трьох значень g (9.8, 9.78, 9.83) (На полюсах вона більше, на екваторі менше).
# Для утворення всіх потрібних комбінацій ідеально підійдуть sets та Декартовий добуток. Я отримую всі можливі 
# комбінації пар для множини з довжин і множини з g

pi = math.pi

# return T (period) in seconds
def time_period(length: int, g:int):
  return 2*pi*math.sqrt(length/g)

length_values = FiniteSet(15, 18, 21, 22.5, 25)
g_values = FiniteSet(9.8, 9.78, 9.83)

all_combinations = length_values * g_values
# (22.50, 9.78), (15.00, 9.78), (22.50, 9.80), (18.00, 9.78), (15.00, 9.80), (22.50, 9.83), (21.00, 9.78), 
# (18.00, 9.80), (15.00, 9.83), (25.00, 9.78), (21.00, 9.80), (18.00, 9.83), (25.00, 9.80), (21.00, 9.83), (25.00, 9.83)


print('{0:^15}{1:^15}{2:^15}'.format('Length(cm)', 'Gravity(m/s^2)', 'Time  Period(s)')) 

for pair in all_combinations:
    l = pair[0]
    g = pair[1]
    t = time_period(l/100, g)
    print('{0:^15}{1:^15}{2:^15.3f}'.format(float(l), float(g), float(t))) 
