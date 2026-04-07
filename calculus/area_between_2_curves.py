from sympy import Symbol, Integral
from dataclasses import dataclass

# Інтеграл можна використовувати для пошуку площі під кривою.
# І якщо у нас є дві функція, одна з яких вище, а друга нижче, то якщо я обрахую
# площу кожної з них і від вищої відніму нижчу то отримую площу фігури яка утвориться
# при перетинанні площ цих підінтегральних функцій
# 
# Розглянемо задачу де у мене є функція f(x)=kx і f(x)=x^2
# 

@dataclass
class function_data:
  fx: any
  x: Symbol
  a: int
  b: int


def area_between_2_curves(func1:function_data,func2:function_data):
  area1 = Integral(func1.fx, (func1.x, func1.a, func1.b)).doit()
  area2 = Integral(func2.fx, (func1.x, func2.a, func2.b)).doit()

  print(f"Area of func1 is: {area1}")
  print(f"Area of func2 is: {area2}")
  return abs(area1-area2)


x1 = Symbol('x')
fx1 = x1
f1 = function_data(
  fx=fx1,
  x=x1,
  a=0,
  b=1,
)

x2 = Symbol('x')
fx2 = x2**2
f2 = function_data(
  fx=fx2,
  x=x2,
  a=0,
  b=1,
)

print(area_between_2_curves(f1, f2)) # 1/6