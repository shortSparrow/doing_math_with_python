from matplotlib import pyplot as plt 
from matplotlib import animation

# Тут показано базовий приклад анімації у matplotlib

def create_circle():
    circle = plt.Circle((0, 0), 0.05)
    return circle

# frame_idx - це номер поточного кадру, оскільки у нас передано параметр frames=30 то це значить 30 кадрів
def update_radius(frame_idx, circle): 
    circle.radius = frame_idx*0.5
    return circle,

def create_animation(): 
    # plt.gcf() сам по собі ініціалізує полотно, навіть якщо воно поки що порожнє.
    fig = plt.gcf()
    ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10)) 
    ax.set_aspect('equal')
    circle = create_circle()
    ax.add_patch(circle)

    # interval - затримка між кожним кадром у м/с
    # frames - кількість кадрів, можна навіть передати власний список кадрів frames=[1, 2, 5, 10, 20] 
    # fargs — це спосіб передати у вашу функцію update_radius додаткові об'єкти, з якими вона має працювати. 
    #   Назва розшифровується як "function arguments" (аргументи функції).
    #   За замовчуванням FuncAnimation передає у функцію лише одне число — номер кадру (i). 
    #   Але вашій функції update_radius потрібно щось більше: їй потрібно знати, яке саме коло (об'єкт circle) 
    #   вона має змінювати.
    # 
    # ми повинні зберегти animation.FuncAnimation у змінну, бо інакше garbage collector видалить це і не буде анімації
    anim = animation.FuncAnimation(fig, update_radius, fargs = (circle,), frames=30, interval=50) 
    plt.title('Simple Circle Animation')
    plt.show()


create_animation()