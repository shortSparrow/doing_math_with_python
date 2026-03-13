import matplotlib.pyplot as plt
def fibo(n): 
    if n == 1: 
        return [1]
    if n == 2:
        return [1, 1]
    # n > 2
    a = 1
    b = 1
    # First two members of the series 
    series = [a, b]
    for i in range(n):
        c = a + b
        series.append(c) 
        a = b
        b = c
    return series 

sequence = fibo(100)
values = []
    
for index, value in enumerate(sequence):
    if(index + 1 < len(sequence)):
        values.append(sequence[index+1]/value)

plt.plot(values)
plt.show()