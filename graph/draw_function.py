import matplotlib.pyplot as plt
# Малювання графіка функції квадратного рівняння

def equation(x:int):
  return x**2 + 2*x + 1 

x_values = range(1,20,1)
y_values = [equation(x) for x in x_values]

plt.plot(x_values, y_values, marker='o')
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# def draw__graph():
