from sympy import Symbol, solve
from sympy.plotting import plot

# solve - вирішує рівняння

x = Symbol('x')

expr2 = x - 5 - 7 # це означає, що x - 5 - 7 = 0
print(solve(expr2)) # [12]

expr3 = x**2 + 5*x + 4 # Квадратне рівняння має два корені
print(solve(expr3, dict=True)) # [{x: -4}, {x: -1}]

expr4 = x**2 + x + 1 # Це рівняння не має дійсних коренів, але має комплексні корені
print(solve(expr4, dict=True)) # [{x: -1/2 - sqrt(3)*I/2}, {x: -1/2 + sqrt(3)*I/2}]


# Система рівнянь
# Нехай буде така система
# 2x + 3y = 6 
# 3x + 2y = 12
x1 = Symbol('x') 
y1 = Symbol('y') 
expr1 = 2*x1 + 3*y1 - 6
expr2 = 3*x1 + 2*y1 - 12

print(solve((expr1, expr2), dict=True)) # [{x: 24/5, y: -6/5}]



# Можна намалювати графік функції (виразу/рівняння)
# plot(2*x+3)
plot(2*x+3, 3*x+1) # намалювати кілька функцій