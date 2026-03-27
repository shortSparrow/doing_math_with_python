import matplotlib.pyplot as plt   
import matplotlib.cm as cm        
import random                     
   
def initialize_image(x_p, y_p):   
  image = []                    
  for i in range(y_p):      
    x_colors = []             
    for j in range(x_p):      
      x_colors.append(0)    
    image.append(x_colors)  

  # image тут масив масивів нулів [[0,0,0,0...], [0,0,0,0...], ...]
  return image             
                                  
def color_points():               
  x_p = 6                       
  y_p = 6                       
  image = initialize_image(x_p, y_p)   
  for i in range(y_p):
    for j in range(x_p):
      # Заповнюємо image випадковими числами від 1 до 10, це будуть наші кольори 
      image[i][j] = random.randint(0, 10)

  # imshow робить з масиву масивів чисел зображення, тобто ми передали масив пікселів і imshow зробить з нього картинку 
  # 
  # origin='lower', За замовчуванням (top). Комп'ютерні зображення зазвичай рахуються зверху зліва, 
  # тобто індекс [0][0] — це лівий верхній кут.  lower: Змінює логіку на "декартову". 
  # Тепер індекс [0][0] — це лівий нижній кут (початок координат). Це робить картинку схожою на звичайний графік функцій.
  # 
  # extent=(0, 5, 0, 5) Цей параметр каже: "Розтягни мою матрицю на конкретні координати графіка". 
  # Формат: (left, right, bottom, top)
  # 
  # cmap=cm.Greys_r
  # Це Colormap (колірна карта). Вона визначає, в який колір розфарбувати числа.
  # cm.Greys: 0 — білий, 10 — чорний.
  # cm.Greys_r: (літера r означає reverse) 0 — чорний, 10 — білий.
  # 
  # interpolation='nearest' Це те, що відповідає за "квадратики", які ми бачимо на виході
  # nearest: Малює кожен елемент масиву як чіткий квадрат. Колір різко обривається на межі пікселя. 
  # Це ідеально, коли треба бачити точні значення кожної клітинки.
  # 
  # bilinear або bicubic: Якщо поставити ці значення, Matplotlib почне "змішувати" кольори сусідніх клітинок. 
  # Квадратики зникнуть, і ми отримаємо плавний туманний градієнт.

  plt.imshow(image, origin='lower', extent=(0, 5, 0, 5), cmap=cm.Greys_r, interpolation='nearest')     
  plt.colorbar()
  plt.show()

color_points()