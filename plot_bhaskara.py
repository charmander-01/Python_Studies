# Jupyter notebook

import math
import matplotlib.pyplot as plt

a = float(input("Type the value of a: "))
b = float(input("Type the value of b: "))
c = float(input("Type the value of c: "))

if a==0:
    print("The value of a can't be zero")
else:
    delta = b*b - 4*a*c
    if delta>0:
        print("\nTwo real roots")
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        xv = (x1 + x2)/2.0
        yv = (-delta)/(4*a)
        print(x1, x2)
        print("x vertex:", xv)
        print("y vertex:", yv)
    if delta<0:
        print("\nThere aren't real roots")

    x = []
    y = []

    start = int(xv - 10)
    end = int(xv + 10)

    for i in range(start, end):
        x.append(i)
        y.append(a*i*i+ b*i + c)

    plt.plot(x, y)

    # Adicionando títulos e rótulos
    plt.title('Parábola')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')

    plt.grid(True)  # Adiciona uma grade ao gráfico para melhor visualização
    plt.axhline(0, color='red',linewidth=1)  # Adiciona a linha do eixo X
    plt.axvline(0, color='red',linewidth=1)  # Adiciona a linha do eixo Y
    ## plt.show()
