import matplotlib.pyplot as plt

# Цей код показує як можна намалювати кілька кіл вписати їх у квадрат

r = 0.5
def draw_figure(width, height):
  ax = plt.gca() 
  for i in range(height):
    for j in range(width):
      x=j*2*r
      y=i*2*r
      circle = plt.Circle((x, y), radius = r)
      ax.add_patch(circle) 

draw_figure(5,5)
plt.axis('scaled') 
plt.show()
