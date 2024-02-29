import matplotlib.pyplot as plt
import numpy as np

def cubic_function(x):
    return x**3 - 6*x**2 + 11*x - 6

def cubic_derivative(x):
    return 3*x**2 - 12*x + 11

def quadratic_function(x):
    return x**2 - 4*x + 4

def quadratic_derivative(x):
    return 2*x - 4

def newtons_method(func, derivative, initial_guess, tolerance=1e-5, max_iterations=100):
    x = initial_guess
    iterations = 0

    while abs(func(x)) > tolerance and iterations < max_iterations:
        x = x - func(x) / derivative(x)
        iterations += 1

    return x

def plot_convergence(func, derivative, initial_guess):
    x_vals = np.linspace(0, 4, 100)
    y_vals = func(x_vals)

    root = newtons_method(func, derivative, initial_guess)
    plt.scatter(root, 0, color='red', label='Root')
    plt.plot(x_vals, y_vals, label='Function')

    plt.title("Newton's Method Convergence")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    print("Choose a function:")
    print("1. Cubic Function")
    print("2. Quadratic Function")

    choice = input("Enter the number corresponding to the desired function: ")

    if choice == "1":
        func = cubic_function
        derivative = cubic_derivative
    elif choice == "2":
        func = quadratic_function
        derivative = quadratic_derivative
    else:
        print("Invalid choice. Defaulting to Cubic Function.")
        func = cubic_function
        derivative = cubic_derivative

    initial_guess = float(input("Enter the initial guess: "))
    plot_convergence(func, derivative, initial_guess)
