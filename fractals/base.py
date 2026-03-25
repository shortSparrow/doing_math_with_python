import matplotlib.pyplot as plt
import random

# Фрактали це складні самоподібні структури які виходять з простих математичних формул. 
# В основі створення фракталу лежить геометрична трансформація, уявимо що у нас є точка
# P(x, y), на x-y площині, ми пропускаємо її через трансформацію P(x, y) -> Q(x + 1, y + 1) 
# І так точку P ми трансформували у точку Q, а її у точку Q2, а її у точку Q3 і так далі 
# 
# Але у нас буде не одне правило трансформації, а кілька різних
# Rule 1: P1 (x, y) -> P2 (x + 1, y − 1)
# Rule 2: P1 (x, y) -> P2 (x + 1, y + 1)  
# І вони застосовуються з певною імовірністю n раз у випадковому порядку
# 
# Тут показано приклад почергового застосування трансформації з Rule 1 та Rule 1 
# Цей код не генерує фрактал, але дає базове розуміння основи, того як будувати фрактали


def transformation_1(p):
    x = p[0]
    y = p[1]
    return x + 1, y - 1

def transformation_2(p):
    x = p[0]
    y = p[1]
    return x + 1, y + 1 
    
def transform(p):
    # List of transformation functions
    transformations = [transformation_1, transformation_2]
    # Pick a random transformation function and call it 
    t = random.choice(transformations)
    x, y = t(p)
    return x, y

def build_trajectory(p, n):
    x = [p[0]]
    y = [p[1]]
    for i in range(n):
        p = transform(p)
        x.append(p[0])
        y.append(p[1])
    
    return x, y


# Initial point 
p = (1, 1)
n = int(input('Enter the number of iterations: ')) 
x, y = build_trajectory(p, n)
# Plot
plt.plot(x, y) 
plt.xlabel('X')
plt.ylabel('Y') 
plt.show()



