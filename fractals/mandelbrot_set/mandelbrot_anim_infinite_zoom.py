import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import cm

# Налаштування
res = 300  # Роздільна здатність (чим більше, тим повільніше рахує)
max_iter = 100 # Для 150 можна буде далі зазумитися. Коли ти зумишся глибше, межа фракталу стає складнішою. Точки, які знаходяться дуже близько до множини, потребують набагато більше перевірок, щоб зрозуміти, чи "втечуть" вони в нескінченність. Якщо ліміт малий, алгоритм вважає їх частиною множини (чорними).
frames = 60  # Кількість кадрів

# Точка, в яку ми будемо "пірнати" (можна змінювати)
target_x, target_y = -0.743643887037158, 0.131825904205312
zoom_factor = 0.9 # На скільки звужується вікно кожен кадр

fig, ax = plt.subplots(figsize=(8, 8))
# Початкове положення
x_min, x_max = -2.0, 0.5
y_min, y_max = -1.25, 1.25

def calculate_mandelbrot(x_min, x_max, y_min, y_max, res, max_iter):
    # Використовуємо numpy для швидкості
    x = np.linspace(x_min, x_max, res)
    y = np.linspace(y_min, y_max, res)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C)
    img = np.zeros(C.shape, dtype=float)
    mask = np.full(C.shape, True, dtype=bool)

    for i in range(max_iter):
        Z[mask] = Z[mask] * Z[mask] + C[mask]
        # Знаходимо точки, які "втекли"
        escaped = np.abs(Z) > 2
        # Записуємо кількість ітерацій для тих, що втекли саме зараз
        newly_escaped = escaped & mask
        img[newly_escaped] = i
        mask[escaped] = False
    
    return img

# Створюємо базовий об'єкт зображення
img_data = calculate_mandelbrot(x_min, x_max, y_min, y_max, res, max_iter)
im = ax.imshow(img_data, extent=(x_min, x_max, y_min, y_max), cmap=cm.magma, origin='lower')
ax.axis('off')

def update(frame):
    global x_min, x_max, y_min, y_max
    
    # Розраховуємо нові межі для ефекту зуму
    width = (x_max - x_min) * zoom_factor
    height = (y_max - y_min) * zoom_factor
    
    # Центруємо вікно навколо цільової точки
    x_min = target_x - width / 2
    x_max = target_x + width / 2
    y_min = target_y - height / 2
    y_max = target_y + height / 2
    
    # Перераховуємо фрактал
    new_img = calculate_mandelbrot(x_min, x_max, y_min, y_max, res, max_iter)
    im.set_data(new_img)
    im.set_extent((x_min, x_max, y_min, y_max))
    return [im]

# Створення анімації
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.title("Mandelbrot Zoom")
plt.show()