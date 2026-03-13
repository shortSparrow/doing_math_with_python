import math
import matplotlib.pyplot as plt

# Візуалізація траєкторії кинутого м'яча по параболі (опором повітря нехтуємо)
# 
# Ми можемо описати траєкторію кинутого м'яча, якщо розділимо Vx та Vy, тобто
# швидкість по x та по y. Отже уявимо що кут між цими двома векторами руку буде θ.
# 
# Vx - вектор руху по осі x (опором повітря нехтуємо, тому вона константна)
# Vy - вектор руху по осі y (їй протидія сила тяжіння gt)
# θ - кут між вектором Vx та Vy
# gt - сила тяжіння що діє на кинутий предмет на вектор Vy
# u - початкова швидкість
#
# Vx = u * cosθ
# Vy = u * sinθ - gt
# 
# Sx = u * cosθ * t
# Sy = hy = (u * sinθ * t) - (g*t^2)/2
#
#
# Тепер нам треба дізнатися як довго наш м'яч буде знаходитися у повітрі.
# М'яч досягне максимальної висоти (вершити параболи), коли його Vy = 0
# Vy = u * sinθ - gt = 0
# t = u * sinθ / g
# Це час який знадобиться щоб витратити всю кінетичну енергію на досягнення висоти. А час 
# який м'яч витрати на повернення до низу буде такий самий
# t(польоту) = 2 * u * sinθ / g
#
# Для візуалізації будемо розраховувати точку польоту м'яча кожну 0.001 секунду
# Нехай:
#   початкова швидкість буде 20 м/с
#   кут кидання θ 45 градусів
#
#
#
#
#


def draw_graphic(v0:int, teta: float, disable_auto_scale=False):
    g = 9.8
    t_flight = 2 * v0 * math.sin(teta) / g

    # range не підтримує float increment, тому щоб працювати з числами з плаваючою точкою є ця функція
    def frange(start, final, increment):
        numbers = []
        while start < final:
            numbers.append(start)
            start = start + increment
        
        return numbers


    time = frange(0, t_flight, 0.001)
    x_coords = [ v0 * math.cos(teta) * t  for t in time]
    y_coords = [ (v0 * math.sin(teta) * t) - (g*t*t)/2  for t in time]

    if disable_auto_scale:
        plt.xlim(0, 45) # Фіксуємо дальність (наприклад, до 45 метрів)
        plt.ylim(0, 15) # Фіксуємо висоту (наприклад, до 15 метрів)
        plt.gca().set_aspect('equal', adjustable='box') # Робимо масштаб 1:1

    plt.plot(x_coords, y_coords,)
    plt.xlabel("Координати x - довжина у м")
    plt.ylabel("Координати y - висота у м")



# Політ під одним кутом, але з різною швидкістю
# draw_graphic(10, math.radians(30))
# draw_graphic(20, math.radians(30))
# draw_graphic(30, math.radians(30))
# plt.legend([10,20,30])

# Політ під одним різними кутами з однією швидкістю
# draw_graphic(20, math.radians(10))
# draw_graphic(20, math.radians(20))
# draw_graphic(20, math.radians(30))
# plt.legend(["10°","20°","30°"])

draw_graphic(10, math.radians(85), True)
draw_graphic(20, math.radians(45), True)
draw_graphic(100, math.radians(5), True)
plt.legend(["85°","45°","5°"])


plt.show()

