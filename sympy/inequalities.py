
from sympy import Poly, Symbol, sin, solve_poly_inequality, solve_rational_inequalities, solve_univariate_inequality

# sympy може також вирішувати нерівності
# Функції для розв'язання нерівностей доступні у вигляді трьох окремих 
# функцій для поліноміальних, раціональних (polynomial, rational) та всіх інших нерівностей. 
# Нам потрібно буде вибрати правильну функцію для розв'язання різних нерівностей, інакше ми отримаємо помилку.


# Поліном (polynomial) — це алгебраїчний вираз, що складається з змінної та коефіцієнтів і містить лише операції 
# додавання, віднімання та множення, а також лише додатні степені змінної. Прикладом поліноміального нерівності є 
# x² + 4 < 0. 
# для вирішення такої нерівності використовується solve_poly_inequality

# Раціональне вираження — це алгебраїчне вираження, у якому чисельник і знаменник є поліномами. Ось приклад раціональної нерівності 
# (x-1)/(x+2) > 0
# для вирішення такої нерівності використовується solve_rational_inequalities()

# Універсальні нерівності такі як sin(x) > 0.5, для них використовується метод solve_univariate_inequality


def solve_polynomial(inequalities):
  left_part = inequalities.lhs
  p = Poly(left_part, x)
  operator = inequalities.rel_op # дістаємо оператор (знак > чи <)
  return solve_poly_inequality(p, operator)

def solve_rational(inequalities):
  left_part = inequalities.lhs
  numer, denom = left_part.as_numer_denom()
  p1 = Poly(numer) 
  p2 = Poly(denom) 
  operator = inequalities.rel_op
  return solve_rational_inequalities([[((p1, p2), operator)]])

def solve_universal(inequalities, x):
  solve_univariate_inequality(inequalities, x, relational=False)


def general_solve(inequalities, x):
  if inequalities.is_polynomial():
    return solve_polynomial(inequalities)

  if inequalities.is_rational_function():
    return solve_rational(inequalities)
  
  return solve_univariate_inequality(inequalities, x)


x = Symbol('x')

# Поліноміальні нерівності
print(solve_polynomial(x + 5 - 3 > 0 )) # x + 5 > 3 => але треба переробили  щоб справа був 0, то маємо x + 5 - 3 > 0
print(solve_polynomial(-x**2 + 4 < 0 ))

# раціональні нерівності
print(solve_rational(((x-1)/(x+2)) > 0))

# універсальні нерівності
ineq_obj = sin(x) - 0.6 > 0
print(solve_universal(ineq_obj, x))
