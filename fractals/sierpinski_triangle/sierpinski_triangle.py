import matplotlib.pyplot as plt
import random

# Трикутник Семінського
# У нас будуть такі правила трансформації
# Transformation 1 (1/3 probability): 
#   xₙ₊₁ = 0.5Xₙ
#   yₙ₊₁ = 0.5yₙ
# 
# Transformation 2 (1/3 probability)
#   xₙ₊₁ = 0.5xₙ + 0.5
#   yₙ₊₁ = 0.5yₙ + 0.5
# 
# Transformation 3 (1/3 probability): 
#   xₙ₊₁ = 0.5xₙ + 1
#   yₙ₊₁ = 0.5yₙ
# 
# 
# 
# В цьому прикладі не будемо писати свою функцію функцію для розподілу імовірностей, а візьмемо вже готовий 
# механізм із пайтона random.choices
# 
# Як ми бачимо завдяки різним кольорам Transformation 1 відповідає за лівий трикутник, 
# Transformation 2 за верхній, а Transformation 3 за правий 
# 
# Для того, аби подивитися як утворюється самоподібність варто подивитися анімацію в
# .fractals/sierpinski_triangle/sierpinski_triangle_anim.py
# 
# Ми можемо змінювати коефіцієнти параметрів і тим самим змінювати форму і розмір трикутника

def transformation_1(x: int, y: int): return (x*0.5, y*0.5)
def transformation_2(x: int, y: int): return (x*0.5 + 0.5, y*0.5 + 0.5)
def transformation_3(x: int, y: int): return (x*0.5 + 1, y*0.5)


transformations = [transformation_1, transformation_2, transformation_3]
weights = [1/3, 1/3, 1/3] # Ймовірності
colors=["red", "green", "blue"]


def draw_fractal(count: int):
  x = 0
  y = 0

  points_x = []
  points_y = []
  point_colors = []

  for i in range(count):
    # k=1 означає, що нам потрібен один результат
    # Оскільки функція повертає список, беремо [0] елемент
    idx = random.choices(range(len(transformations)), weights=weights, k=1)[0]
    x1,y1 = transformations[idx](x,y)
    color = colors[idx]
    x=x1
    y=y1

    points_x.append(x1)
    points_y.append(y1)
    point_colors.append(color)

  # цей метод малює тільки одним кольором, тож якщо нам не треба різні кольори для різних трансформацій він підійде
  # plt.plot(points_x, points_y, 'o', markersize=1, color='green')

  fig, ax = plt.subplots()
  ax.scatter(points_x, points_y, s=0.5, c=point_colors, edgecolors='none')

  plt.show()

draw_fractal(50000)