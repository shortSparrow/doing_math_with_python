import csv
from pathlib import Path
import statistics
import matplotlib.pyplot as plt


def read_csv(filename):
    with open(filename, encoding='utf-8') as f: 
        reader = csv.reader(f)
        
        # 1. Отримуємо перший рядок (заголовок) окремо
        header = next(reader)
        
        # 2. Витягуємо роки (вони починаються з індекса 4)
        years = header[4:] 
        
        population = []
        
        # 3. Тепер reader продовжує читання з ДРУГОГО рядка
        for row in reader:
            if row[0] == "Ukraine":
                population = [float(val) if val else 0.0 for val in row[4:]]
                break 
        
        return years, population

# Отримуємо шлях до теки, де лежить поточний файл
script_dir = Path(__file__).parent
file_path = script_dir / "population_by_years.csv"
(years, population) = read_csv(file_path)



# Середнє арифметичне
mean_val = statistics.mean(population)
median_val = statistics.median(population)
stdev_val = statistics.stdev(population)

print(f"Середнє: {mean_val:.2f}")
print(f"Медіана: {median_val:.2f}")
print(f"Станд. відхилення: {stdev_val:.2f}")


plt.plot(years, population)
plt.ticklabel_format(style='plain', axis='y') # прибираємо наукову нотацію і пишемо цифри по нормальному
plt.xticks(years[::10], rotation=45) # По осі x беру крок у 10 років і малюю роки під кутом 45 градусів, бо років дуже багато, всі не вміщаються
plt.show()

