import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

def transformation_1(p): return (p[0] * 0.5, p[1] * 0.5)
def transformation_2(p): return (p[0] * 0.5 + 0.25, p[1] * 0.5 + 0.5)
def transformation_3(p): return (p[0] * 0.5 + 0.5, p[1] * 0.5)

transformations = [transformation_1, transformation_2, transformation_3]
weights = [1/3, 1/3, 1/3]
colors_map = ['#FF4136', '#2ECC40', '#0074D9'] 

# Початкові дані
point = (0.5, 0.5)
points_x = []
points_y = []
points_colors = []

# Налаштування графіки
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off') # Ховаємо осі для краси
ax.set_title("Sierpinski Triangle: Color Coded Transformations")

# Створюємо scatter об'єкт.
# ми не задаємо 'c' (color) тут, ми будемо оновлювати його динамічно.
scat = ax.scatter([], [], s=0.5, marker=',')

def update(frame):
    global point
    points_per_frame = 100
    
    for _ in range(points_per_frame):
        idx = random.choices(range(len(transformations)), weights=weights, k=1)[0]
        
        trans = transformations[idx]
        point = trans(point)
        
        points_x.append(point[0])
        points_y.append(point[1])
        points_colors.append(colors_map[idx])
    
    # Оновлюємо координати всіх точок
    scat.set_offsets(list(zip(points_x, points_y)))
    
    # set_color приймає список кольорів тієї ж довжини, що і кількість точок
    scat.set_color(points_colors)
    
    return scat,

# Налаштування анімації
# blit=True дуже важливий для продуктивності при зміні кольорів
ani = FuncAnimation(fig, update, frames=200, interval=30, blit=True, repeat=False)

plt.show()