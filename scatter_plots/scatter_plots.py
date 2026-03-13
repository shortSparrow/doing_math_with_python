import sys
import os

# Отримуємо шлях до папки, де лежить цей скрипт (scatter_plots)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Отримуємо шлях до батьківської папки (doing_math_with_python)
project_root = os.path.dirname(current_dir)

# Додаємо корінь проєкту в sys.path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import matplotlib.pyplot as plt
import math
from dispersion.variance_and_standard_deviation import variance
from dispersion.pearson_correlation_coefficient import find_corr_x_y

# scatter plot можуть бути корисними не лише як візуалізація, але і як наочне розуміння
# того де знаходяться величини, що ми виміряємо. Для наочності додамо 4 різних набори
# даних, які мають однаковий mean, variance, pearson correlation coefficient. Цей набір
# називається Anscombe’s quartet.


A_x = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
A_y = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

B_x = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
B_y = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]

C_x = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
C_y = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]

D_x = [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 19.0, 8.0, 8.0, 8.0]
D_y = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]

print("set A: ")
print("variance A_x: ", variance(A_x))                    # 10.0
print("variance A_y: ", variance(A_y))                    # 3.75
print("mean A_x: ", sum(A_x)/len(A_x))                    # 9.0
print("mean A_y: ", sum(A_y)/len(A_y))                    # 7.5
print("Pearson correlation A: ", find_corr_x_y(A_x, A_y)) # 0.81

print("----------------------------------")

print("set B: ")
print("variance B_x: ", variance(B_x))                    # 10.0
print("variance B_y: ", variance(B_y))                    # 3.75
print("mean B_x: ", sum(B_x)/len(B_x))                    # 9.0
print("mean B_y: ", sum(B_y)/len(B_y))                    # 7.5
print("Pearson correlation B: ", find_corr_x_y(B_x, B_y)) # 0.81

print("----------------------------------")

print("set С: ")
print("variance C_x: ", variance(C_x))                    # 10.0
print("variance C_y: ", variance(C_y))                    # 3.75
print("mean C_x: ", sum(C_x)/len(C_x))                    # 9.0
print("mean C_y: ", sum(C_y)/len(C_y))                    # 7.5
print("Pearson correlation C: ", find_corr_x_y(C_x, C_y)) # 0.81

print("----------------------------------")

print("set D: ")
print("variance D_x: ", variance(D_x))                    # 10.0
print("variance D_y: ", variance(D_y))                    # 3.75
print("mean D_x: ", sum(D_x)/len(D_x))                    # 9.0
print("mean D_y: ", sum(D_y)/len(D_y))                    # 7.5
print("Pearson correlation D: ", find_corr_x_y(D_x, D_y)) # 0.81

# Побудуємо табличку і побачимо що дані ідентичні
# 
#          X                      Y
#     Mean   variance       Mean    variance    Correlation
# A   9.00     10.0         7.50      3.75         0.81
# B   9.00     10.0         7.50      3.75         0.81
# C   9.00     10.0         7.50      3.75         0.81
# D   9.00     10.0         7.50      3.75         0.81


# Але якщо ми спробуємо побудувати гарфіки з цих даних, то вони будуть геть різні. Тобто навіть якщо
# всі ці показники однакові, графіки і залежності величин можуть бути кардинально різні




# Створюємо сітку 2x2. figsize задає розмір загального вікна
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# axes — це масив об'єктів (графіків). Звертаємося до них за індексами:
# Графік A (зверху зліва)
axes[0, 0].scatter(A_x, A_y, color='red')
axes[0, 0].set_title('Dataset A')

# Графік B (зверху справа)
axes[0, 1].scatter(B_x, B_y, color='green')
axes[0, 1].set_title('Dataset B')

# Графік C (знизу зліва)
axes[1, 0].scatter(C_x, C_y, color='blue')
axes[1, 0].set_title('Dataset C')

# Графік D (знизу справа)
axes[1, 1].scatter(D_x, D_y, color='orange')
axes[1, 1].set_title('Dataset D')

# Автоматично підрівнює відстані між графіками, щоб назви не налізали одна на одну
plt.tight_layout()
plt.show()