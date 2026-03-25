import matplotlib.pyplot as plt

# Тут показано як малювати фігуру. У нас є 
# gca() - get current axis - функція, яка створює об'єкт координатної сітки якщо такої немає і повертає її 
# plt.Circle - функція, яка створює об'єкт кола 
# add_patch() - метод що приймає об'єкт фігури, в нашому випадку коло і додає його до об'єкту з осями

x = [1, 2, 3]
y = [1, 2, 3]


def create_circle():
  circle = plt.Circle((0, 0), radius = 0.5)
  return circle

def show_shape(patch): 
    ax = plt.gca() 
    ax.add_patch(patch) 
    plt.axis('scaled') 
    plt.show()


c = create_circle()
show_shape(c)