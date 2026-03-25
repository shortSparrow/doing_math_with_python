import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

# --- Ваші трансформації (без змін) ---
def transformation_1(x, y): return 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6
def transformation_2(x, y): return 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6
def transformation_3(x, y): return -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44
def transformation_4(x, y): return 0, 0.16*y

def get_probable_index(probability):
    rand = random.random()
    accumulate_prob = 0
    for index, prob in enumerate(probability):
        accumulate_prob += prob
        if rand <= accumulate_prob:
            return index
    return len(probability) - 1

# --- Налаштування анімації ---

fig, ax = plt.subplots(figsize=(6, 10))
ax.set_xlim(-3, 3)
ax.set_ylim(0, 11)
ax.axis('off')

# Створюємо об'єкт "scatter", який спочатку порожній
# s=1 - розмір точки, c='green' - колір
scat = ax.scatter([], [], s=1, c='forestgreen', marker=',')

x_data, y_data = [], []
curr_x, curr_y = 0, 0

transformation_list = [transformation_1, transformation_2, transformation_3, transformation_4]
transformation_probability = [0.85, 0.07, 0.07, 0.01]

def update(frame):
    global curr_x, curr_y
    
    # За один кадр додаємо, наприклад, 50 точок, щоб анімація не була надто повільною
    points_per_frame = 100
    for _ in range(points_per_frame):
        index = get_probable_index(transformation_probability)
        curr_x, curr_y = transformation_list[index](curr_x, curr_y)
        x_data.append(curr_x)
        y_data.append(curr_y)
    
    # Оновлюємо дані на графіку
    scat.set_offsets(list(zip(x_data, y_data)))
    return scat,

# frames - кількість кадрів, interval - затримка в мілісекундах
ani = FuncAnimation(fig, update, frames=300, interval=20, blit=True, repeat=False)

plt.title("Анімація створення папороті Барнслі")
plt.show()