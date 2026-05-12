def f(x):
    return x**2

def derivative(f,x, h=0.00000001):
    return (f(x+h)-f(x))/h

for x in range(-5,6):
    print(x,derivative(f,x))