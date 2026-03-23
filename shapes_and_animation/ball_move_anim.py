from matplotlib import pyplot as plt 
from matplotlib import animation 
import math


# Задача 
# Зробити анімацію польоту м'яча, якщо у ./graph/ball_move.py ми малювали лише графік, то тут 
# треба зробити анімацію по цьому графіку
# 
# Нам треба дізнатися як довго наш м'яч буде знаходитися у повітрі.
# М'яч досягне максимальної висоти (вершити параболи), коли його Vy = 0
# Vy = u * sinθ - gt = 0
# t = u * sinθ / g
# Це час який знадобиться щоб витратити всю кінетичну енергію на досягнення висоти. А час 
# який м'яч витрати на повернення до низу буде такий самий
# t(польоту) = 2 * u * sinθ / g
#

g = 9.8

# У нас буде сталий інтервал затримки на кожен кадр, це 15 м/с, воно прописано у animation.FuncAnimation як параметр. 
# get_intervals - Фізичні формули x(t) та y(t) не працюють без значення t. Функція get_intervals створює список усіх 
# значень t, які будуть підставлені у формулу для кожного окремого кадру. Тобто це список часових проміжків 
# для яких ми рахуємо значення (це масив від 0 до t_flight з кроком у 0.05, з range таке зробити не можна бо він не 
# працює із float, лише з int)
def get_intervals(u, theta):
    t_flight = 2*u*math.sin(theta)/g 
    intervals = []
    start = 0
    interval = 0.05
    while start < t_flight:
        intervals.append(start)
        start = start + interval 

    return intervals

def update_position(i, circle, intervals, u, theta): 
    t = intervals[i]
    x = u*math.cos(theta)*t
    y = u*math.sin(theta)*t - 0.5*g*t*t 
    circle.center = x, y

    # Розрахунок миттєвої швидкості для терміналу
    vx = u * math.cos(theta)
    vy = u * math.sin(theta) - g * t
    v_total = math.sqrt(vx**2 + vy**2)
    
    # Виводимо в термінал (використовуємо \r, щоб рядок оновлювався на місці, а не спамив)
    print(f"Кадр: {i:3} | Час: {t:.2f}с | Vy: {vy:6.2f} м/с | Загальна швидкість: {v_total:6.2f} м/с", end='\r')

    return circle

def create_animation(u, theta):
    intervals = get_intervals(u, theta)

    # Для того щоб визначити межі анімації там треба визначити мінімальні і максимальні координати по x та y. 
    # Мінімальна координата 0, а максимальна для x - це початкова швидкість для осі x * час польоту 
    # тобто для x буде Vx*t_flight = u*cos(theta)*t_flight -> Vx0 * час польоту
    # а для y буде u*sin(theta) - gt^2/2 - це виходить Vx0 -> прискорення вільного падіння яке діє у протилежну сторону 
    xmin = 0
    xmax = u*math.cos(theta)*intervals[-1] 
    ymin = 0
    t_max = u*math.sin(theta)/g
    ymax = u*math.sin(theta)*t_max - (g*t_max**2)/2

    fig = plt.gcf()
    ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
    ax.set_aspect('equal')
    circle = plt.Circle((xmin, ymin), 1.0) 
    ax.add_patch(circle)
    anim = animation.FuncAnimation(fig, update_position, 
                        fargs=(circle, intervals, u, theta), 
                        frames=len(intervals), interval=15)
  
    plt.title('Projectile Motion') 
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


# Початкова швидкість (у m/s): 
u = float(30)
# Кут під яким було кинуто м'ячик (у градусах):
theta = float(80)

theta = math.radians(theta) 
create_animation(u, theta)