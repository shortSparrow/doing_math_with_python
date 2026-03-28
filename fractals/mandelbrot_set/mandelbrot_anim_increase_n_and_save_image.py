import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import os

# Звузимо область перегляду, бо при від'ємних степенях цікаве відбувається ближче до центру
x_min, x_max = -2.0, 2.0
y_min, y_max = -2.0, 2.0
RESOLUTION = 600  
MAX_ITER_FOR_PIXEL = 100 

OUTPUT_DIR = "mandelbrot_dynamic_n"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# --- Налаштування діапазону ступенів (n) ---
N_START = -10.0
N_END = 15.0
N_STEP = 0.25

# Створюємо масив значень n (кількість кадрів)
n_values = np.arange(N_START, N_END + N_STEP, N_STEP)
total_frames = len(n_values)

# --- Підготовка сітки (NumPy) ---
y_coords, x_coords = np.ogrid[y_min:y_max:RESOLUTION*1j, x_min:x_max:RESOLUTION*1j]
# Cтворюємо матрицю комплексних чисел c для всієї площини одночасно
c_grid = x_coords + 1j * y_coords

# Підготовка фігури (один раз)
fig, ax = plt.subplots(figsize=(10, 10), dpi=100)
ax.axis('off')
# Створюємо порожнє зображення для ініціалізації
img = ax.imshow(np.zeros((RESOLUTION, RESOLUTION)), origin='lower', 
                extent=(x_min, x_max, y_min, y_max), 
                cmap=cm.magma, interpolation='nearest')

# Додамо текст для відображення поточного n на картинці
text_n = ax.text(0.02, 0.95, '', transform=ax.transAxes, color='white', fontsize=14, 
                 bbox=dict(facecolor='black', alpha=0.5, boxstyle='round,pad=0.3'))


# --- Основний цикл генерації (Оптимізований NumPy) ---
print(f"Починаємо збереження {total_frames} кадрів у папку '{OUTPUT_DIR}'...")

frame_count = 0
for n_float in n_values:
    # Запобігаємо помилкам при n=0 або n=1, які можуть давати нецікаві або помилкові результати
    if abs(n_float) < 1e-9: # n == 0
        current_n = 0.0001 # невеличке зміщення
    else:
        current_n = n_float

    # --- NumPy Магія ---
    # Ініціалізуємо z та матрицю ітерацій для поточного n
    z = np.copy(c_grid) # Починаємо з z = c
    diverge_time = np.zeros_like(c_grid, dtype=int) + MAX_ITER_FOR_PIXEL # За замовчуванням всі точки "всередині"
    
    # Маска, яка вказує, які точки ще не розбіглися
    still_in = np.ones_like(c_grid, dtype=bool)

    # Весь цей цикл for працює над ВСІМА пікселями одночасно (векторизовано)
    for i in range(MAX_ITER_FOR_PIXEL):
        # Оновлюємо z тільки для тих точок, які ще не розбіглися
        # Для від'ємних степенів z**n автоматично обчислюється як (1/z)**abs(n)
        # УВАГА: Для від'ємних n і z=0 буде попередження про ділення на 0,
        # але NumPy обробляє це (z стає inf), і abs(z)<2 стає false.
        z[still_in] = z[still_in]**current_n + c_grid[still_in]
        
        # Перевіряємо, які точки розбіглися на цьому кроці (abs(z) > 2)
        diverged_this_step = (np.abs(z) > 2) & still_in
        
        # Записуємо номер ітерації розбіжності
        diverge_time[diverged_this_step] = i
        
        # Оновлюємо маску: залишаємо тільки тих, хто < 2
        still_in[~diverged_this_step] = still_in[~diverged_this_step] & (np.abs(z[~diverged_this_step]) <= 2)
        
        # Якщо всі точки розбіглися, перериваємо цикл ітерацій завчасно
        if not still_in.any():
            break

    # --- Оновлення візуалізації ---
    # Записуємо обчислені ітерації в зображення
    img.set_array(diverge_time)
    
    # Налаштовуємо контрастність
    # Нормалізація залежить від максимальної ітерації. 
    # vmin=0 робить "внутрішню" частину чорною.
    img.set_clim(vmin=0, vmax=MAX_ITER_FOR_PIXEL) 
    
    # Оновлюємо текст із значенням n
    text_n.set_text(f"z = z^{current_n:.2f} + c")
    
    # --- Збереження ---
    frame_count += 1
    # pad_inches=0 та bbox_inches='tight' прибирають білі поля
    file_path = os.path.join(OUTPUT_DIR, f"frame_{frame_count:03d}.png")
    plt.savefig(file_path, bbox_inches='tight', pad_inches=0.02)
    
    if frame_count % 10 == 0:
        print(f"Готово: {frame_count}/{total_frames} (n = {current_n:.2f})")

plt.close(fig) # Закриваємо фігуру
print(f"Всі {total_frames} зображень збережено в '{OUTPUT_DIR}'!")