'''gradient descent is a method used to minimize a function by iteratively 
moving in the direction of the negative gradient of the function.'''

# we have the function f(x)=x**2. We want to find the value of x that minimizes this function.

def f(x):
    return x**2

def df(x):
    return 2*x

def gradient_descent(learning_rate, epsilon, max_iters):
    x = 5.0  # Initial guess for x
    for _ in range(max_iters):
        gradient = df(x)  # Calculate the gradient of the function at x
        if abs(gradient) < epsilon:  # Check for convergence
            break
        x -= learning_rate * gradient  # Update x using gradient descent
    return x

learning_rate = 0.1  # Step size for each iteration
epsilon = 1e-6  # Convergence criterion
max_iters = 1000  # Maximum number of iterations

# Run gradient descent algorithm
optimal_solution = gradient_descent(learning_rate, epsilon, max_iters)

# Print the optimal solution and the value of the objective function at the optimal solution
print("Optimal solution:", optimal_solution)
print("Objective function value at optimal solution:", f(optimal_solution))
