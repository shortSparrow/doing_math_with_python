import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.animation import FuncAnimation

# Тут логіка анімації трохи відрізняється від інших що я робив у ./fractals/...
# У update(frame) ми повністю малюємо катину за один раз, і заповнюємо всі точки кольорами,
# але оскільки параметр current_max_iter у нас динамічний і залежить від номеру frame то ми 
# будемо перемальовувати картину стільки разів скільки у нас фреймів і кожен раз з більшою точністю, 
# бо кожен раз current_max_iter буде збільшуватися і відповідно точність визначення чи належить точка до 
# множини буде більшою

# --- Параметри ---
x_min, x_max = -2.5, 1.0
y_min, y_max = -1.1, 1.1
RESOLUTION = 150  # Менше значення для швидкості анімації без NumPy
MAX_FRAMES = 50    # Скільки кроків (ітерацій) ми покажемо в анімації

# Створюємо порожню матрицю (список списків) для пікселів
# Заповнюємо її нулями
pixels = [[0 for _ in range(RESOLUTION)] for _ in range(RESOLUTION)]

# Готуємо координати заздалегідь, щоб не рахувати їх щоразу
def get_complex_grid(res, x_min, x_max, y_min, y_max):
    grid = []
    step_x = (x_max - x_min) / res
    step_y = (y_max - y_min) / res
    for i in range(res):
        row = []
        for j in range(res):
            x = x_min + j * step_x
            y = y_min + i * step_y
            row.append(complex(x, y))
        grid.append(row)
    return grid

grid_c = get_complex_grid(RESOLUTION, x_min, x_max, y_min, y_max)

# --- Налаштування графіку ---
fig, ax = plt.subplots(figsize=(10, 7))
img = ax.imshow(pixels, origin='lower', extent=(x_min, x_max, y_min, y_max), cmap=cm.magma, interpolation='nearest')
plt.colorbar(img)
ax.set_title("Побудова множини Мандельброта (крок за кроком)")

# --- Функція оновлення ---
def update(frame):
    """
    frame - це номер поточного кадру, ми використаємо його як 
    максимальну кількість ітерацій (max_iteration)
    """
    current_max_iter = frame + 1
    
    # Проходимо по кожному пікселю і визначаємо чи точка належить множині
    for row_idx in range(RESOLUTION):
        for col_idx in range(RESOLUTION):
            c = grid_c[row_idx][col_idx]
            z = 0 + 0j
            iteration = 0
            
            # Рахуємо, чи втече точка за current_max_iter кроків
            while abs(z) < 2 and iteration < current_max_iter:
                z = z*z + c
                iteration += 1
            
            pixels[row_idx][col_idx] = iteration

    # Оновлюємо дані на картинці
    img.set_array(pixels)
    # Оновлюємо колірну шкалу, щоб вона підлаштовувалася під ітерації
    img.set_clim(vmin=0, vmax=current_max_iter)
    
    return [img]

# --- Створення анімації ---
# interval=100 означає 10 кадрів на секунду
ani = FuncAnimation(fig, update, frames=MAX_FRAMES, interval=100, blit=True, repeat=False)

plt.show()


# Коли запустимо анімацію у нас буде мерехтіння кольорів і точки будуть змінювати свої кольори, це тому що
# відбувається автоматичне масштабування кольорової шкали (cmap).
# 
# Варто звернути увагу на current_max_iter
#  
# На 5-му кадрі: 
# Максимальна ітерація = 5. Програма каже: «0 — це чорний, 5 — це яскраво-жовтий». 
# Точка, що втекла за 3 ітерації, буде десь посередині (помаранчева).
# 
# 
# На 50-му кадрі: Максимальна ітерація = 50. Тепер програма каже: «0 — це чорний, а 50 — це яскраво-жовтий». 
# Та сама точка, що втекла за 3 ітерації, тепер становить лише 3/50 від шкали. Вона стає майже чорною, 
# бо вона тепер дуже близько до «мінімуму» порівняно з новими лідерами.
# 
# img.set_clim(vmin=0, vmax=current_max_iter)
# Він змушує графік кожного разу перераховувати, що вважати «максимальним кольором». 
# Оскільки current_max_iter постійно зростає, старі значення (малі числа ітерацій) візуально «тьмяніють» 
# і зсуваються до темного краю палітри.
# 
# 