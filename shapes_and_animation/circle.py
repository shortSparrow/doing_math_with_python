import matplotlib.pyplot as plt

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