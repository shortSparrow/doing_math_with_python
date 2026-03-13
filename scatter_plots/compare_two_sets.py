import matplotlib.pyplot as plt
# from dispersion.pearson_correlation_coefficient import find_corr_x_y

# Нехай у нас є список середнього балу в школі і оцінки екзамену на вступ до коледжу
# Подивимося чи є між ними зв'язок і залежність

# Дані 1: Загальні оцінки (Слабка кореляція ~0.32)
hight_school_grades = [90, 92, 95, 96, 87, 87, 90, 95, 98, 96]
college_exam_grades = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]

# Графік даних показує, що учні з найвищими оцінками в середній школі не обов'язково показували кращі результати 
# на вступних іспитах до коледжу, і навпаки. Деякі учні з низькими оцінками в середній школі дуже добре склали 
# вступні іспити до коледжу, тоді як інші мали відмінні оцінки, але показали відносно погані результати на іспитах до коледжу

# Якщо ми обчислимо коефіцієнт кореляції двох наборів даних (використовуючи нашу програму find_corr_x_y), 
# то побачимо, що він становить приблизно 0,32.
# print(find_corr_x_y(hight_school_grades, college_exam_grades)) # 0.3183



# А тепер візьмемо не загальні оцінки по школі, а лише оцінки з математики
# Дані 2: Математика (Сильна кореляція ~0.99)
hight_school_math_grade = [83, 85, 84, 96, 94, 86, 87, 97, 97, 85]
college_exam_grades = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]

# Видно пряму залежність, а якщо порахуємо коефіцієнт кореляції, то він буде близько 1, що говорить нам, що є лінійна залежність
# print(find_corr_x_y(hight_school_math_grade, college_exam_grades)) # 0.9989



# Створюємо фігуру з двома підграфіками (1 рядок, 2 стовпці)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# --- Лівий графік (Загальні оцінки) ---
ax1.scatter(hight_school_grades, college_exam_grades, color='blue', marker='o')
ax1.set_title("General Grades (Corr ≈ 0.32)")
ax1.set_xlabel("High school grades")
ax1.set_ylabel("College exam grades")
ax1.grid(True, linestyle='--', alpha=0.6) # додамо сітку для наочності

# --- Правий графік (Математика) ---
ax2.scatter(hight_school_math_grade, college_exam_grades, color='red', marker='s')
ax2.set_title("Math Grades (Corr ≈ 1.0)")
ax2.set_xlabel("High school math grades")
# ax2.set_ylabel не обов'язково, бо вони спільні, але можна залишити
ax2.grid(True, linestyle='--', alpha=0.6)

# Підганяємо розміри, щоб написи не перекривалися
plt.tight_layout()
plt.show()