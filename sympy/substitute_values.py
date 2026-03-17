

from sympy import Symbol, pprint

# Підстановка значень у вираз 

x = Symbol('x') 
y = Symbol('y') 
expr = x*x + x*y + x*y + y*y
pprint(expr)
res = expr.subs({x:1, y:2})
print(res) # 9

# Ми також можемо виразити одну змінну чез іншу
res2 = expr.subs({x:1-y})
print(res2) # y**2 + 2*y*(1 - y) + (1 - y)**2
