import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 2*x + 1

def derivative(f, x, h=0.0001):
    return (f(x + h) - f(x)) / h

x = np.linspace(-5, 5, 100)

y = f(x)
true_deriv = 3*x**2 - 2
numerical_deriv = derivative(f, x)

plt.plot(x, y, label="f(x)")
plt.plot(x, true_deriv, label="true derivative")
plt.plot(x, numerical_deriv, label="numerical derivative", linestyle="dashed")
plt.legend()
plt.title("f(x) and its derivative")
plt.xlabel("x")
plt.grid(True)
plt.show()