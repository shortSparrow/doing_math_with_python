import numpy as np
import matplotlib.pyplot as plt
import os

# --- НАЛАШТУВАННЯ ---
res = 1080          
max_iter = 5000      
frames = 300        
zoom_speed = 0.9 
output_dir = "mandelbrot_frames"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

target_x, target_y = -0.743643887037158, 0.131825904205312
x_min, x_max = -2.0, 0.5
y_min, y_max = -1.25, 1.25

def calculate_mandelbrot(x_min, x_max, y_min, y_max, res, max_iter):
    x = np.linspace(x_min, x_max, res)
    y = np.linspace(y_min, y_max, res)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C)
    img = np.zeros(C.shape, dtype=float)
    mask = np.full(C.shape, True, dtype=bool)

    for i in range(max_iter):
        Z[mask] = Z[mask] * Z[mask] + C[mask]
        escaped = np.abs(Z) > 2
        newly_escaped = escaped & mask
        img[newly_escaped] = i
        mask[escaped] = False
    
    return np.log2(img + 1)

fig = plt.figure(figsize=(10, 10), dpi=100)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')

print(f"Починаю рендер {frames} кадрів у папку '{output_dir}'...")

for frame in range(frames):
    # Розрахунок меж
    width = (x_max - x_min) * zoom_speed
    height = (y_max - y_min) * zoom_speed
    
    x_min = target_x - width / 2
    x_max = target_x + width / 2
    y_min = target_y - height / 2
    y_max = target_y + height / 2
    
    # Генерація зображення
    img_data = calculate_mandelbrot(x_min, x_max, y_min, y_max, res, max_iter)
    
    # Малювання
    ax.clear()
    ax.axis('off')
    ax.imshow(img_data, cmap='magma', origin='lower', interpolation='bilinear')
    
    # Збереження
    file_path = os.path.join(output_dir, f"frame_{frame:04d}.png")
    plt.savefig(file_path, bbox_inches='tight', pad_inches=0)
    
    if frame % 5 == 0:
        print(f"Готово: {frame}/{frames} ({(frame/frames)*100:.1f}%)")

plt.close()
print(f"Рендер завершено! Всі кадри в папці {output_dir}")