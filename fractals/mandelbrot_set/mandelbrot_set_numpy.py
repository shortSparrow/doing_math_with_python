import matplotlib.pyplot as plt 
import matplotlib.cm as cm
import numpy as np

# Це той самий код, що і у ./fractals/mandelbrot_set/mandelbrot_set.py але сітка пікселів 
# створена за допомогою numpy щоб було швидше ніж вкладений цикл

# Параметри вікна
x_min, x_max = -2.5, 1.0
y_min, y_max = -1.0, 1.0
resolution = 400
max_iteration = 1000

# Створюємо сітку значень (рівномірно розподіляємо 400 точок між min та max)
x_coords = np.linspace(x_min, x_max, resolution)
y_coords = np.linspace(y_min, y_max, resolution)

# Створюємо порожнє зображення (матрицю)
pixels = np.zeros((resolution, resolution))

for k, y in enumerate(y_coords):
    for i, x in enumerate(x_coords):
        z = 0 + 0j
        c = complex(x, y)
        
        iteration = 0
        
        # Цикл ітерацій (алгоритм "втечі")
        while abs(z) < 2 and iteration < max_iteration:
            z = z*z + c
            iteration += 1
        
        pixels[k, i] = iteration

# Візуалізація
plt.figure(figsize=(10, 7))
# Використовуємо cmap=cm.magma для гарного вигляду, або cm.binary_r для чорно-білого як в інструкції
# extent - цей параметр каже:(left, right, bottom, top)
plt.imshow(pixels, origin='lower', extent=(x_min, x_max, y_min, y_max), cmap=cm.magma)
plt.colorbar()
plt.title("Mandelbrot Set")
plt.show()