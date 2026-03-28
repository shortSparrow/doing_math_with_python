# Doing Math with Python (Amit Saha) — Notes & Exercises

Цей репозиторій містить мої власні нотатки, приклади коду та розв'язання вправ з книги **"Doing Math with Python"** автора **Amit Saha**.

Мета проєкту — вивчення математичних концепцій (алгебра, статистика, ймовірність, фрактали) за допомогою Python та візуалізації результатів.

---

## 📚 Про книгу

Книга навчає використовувати Python для:
- Роботи з числами, дробами та комплексними числами
- Візуалізації даних за допомогою **Matplotlib**
- Символьних обчислень з бібліотекою **SymPy**
- Розв'язання задач зі статистики та теорії ймовірностей
- Побудови геометричних фігур та фракталів

---

## 🛠 Технології

- **Python 3.x**
- **Matplotlib**
- **SymPy**

---

## 📈 Графіки та фізичні моделі

### ⚽ Політ м'яча
Моделювання руху тіла під дією гравітації. Описується рівняннями руху:
$$x = u t \cos(\theta), \quad y = u t \sin(\theta) - \frac{1}{2}gt^2$$

<div align="center">
  <table>
    <tr>
      <th align="center">Траєкторія (Статика)</th>
      <th align="center">Симуляція (Анімація)</th>
    </tr>
    <tr>
      <td align="center" valign="middle">
        <img width="450" src="https://github.com/user-attachments/assets/9a485091-fb93-4da0-b714-398d40366445" />
      </td>
      <td align="center" valign="middle">
        <video width="450" src="https://github.com/user-attachments/assets/bc160b0d-dd87-4e42-b654-77f6d216c109"></video>
      </td>
    </tr>
  </table>
</div>

---

## 🎲 Ймовірність та випадкові процеси

### 🎯 Метод Монте-Карло
Чисельне моделювання випадкових процесів для оцінки ймовірностей.

---

## 📊 Статистика

### 📉 Основні метрики
* **Середнє значення (mean)**: $\bar{x} = \frac{\sum x_i}{n}$
* **Дисперсія**: $\sigma^2 = \frac{\sum (x_i - \bar{x})^2}{n}$
* **Стандартне відхилення** ($\sigma$)
* **Кореляція Пірсона** (оцінка лінійного зв'язку між величинами): $r_{xy} = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2 \sum(y_i - \bar{y})^2}}$

---

## 🌌 Фрактали

### 🌿 Папороть Барнслі та 🔺 Трикутник Серпінського
<div align="center">
  <img width="380" src="https://github.com/user-attachments/assets/717dcbdb-7fbd-43bf-b2b6-60e7578a8a5a" alt="Barnsley Fern" />
  <img width="450" src="https://github.com/user-attachments/assets/eea9aa07-6e7b-4df7-b9ef-17593e6500de" alt="Sierpinski Triangle" />
</div>

---

### 🌌 Множина Мандельброта
Візуалізація комплексної площини для формули $z_{n+1} = z_n^d + c$.

<p align="center">
  <img width="80%" src="https://github.com/user-attachments/assets/dc829a42-75da-4b6e-9b9a-14098c7f3f4d" />
</p>

**Різні варіації:**
<div align="center">
  <table>
    <tr>
      <th align="center">Зум із параметром max_iteration=5000</th>
      <th align="center">Степінь d = 1 → 100 із кроком в 1, та параметром max_iteration=d</th>
      <th align="center">Степінь d = -2 → 2 із кроком в 0.1</th>
    </tr>
    <tr>
      <td align="center">
        <video width="280" src="https://github.com/user-attachments/assets/7152ed49-462c-44a5-bbdc-1878a51a7c55"></video>
      </td>
      <td align="center">
        <video width="280" src="https://github.com/user-attachments/assets/60152415-155b-4ec9-8a40-fd8ce3d684e0"></video>
      </td>
      <td align="center">
        <video width="280" src="https://github.com/user-attachments/assets/2a166244-2b40-4e4a-812d-a4ba4054a172"></video>
      </td>
    </tr>
  </table>
</div>

---

## 🧠 Призначення проєкту
- Практичне розуміння математики через код
- Візуалізація складних концепцій
- Закріплення Python через реальні задачі
- Основа для подальших експериментів
