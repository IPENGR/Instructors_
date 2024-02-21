# Define a decorator function 'extra_add' that takes a function 'f' as an argument.
def extra_add(f):
    # Define an inner function 'inner' that takes two arguments 'x' and 'y'.
    def inner(x, y):
        # Check if both 'x' and 'y' are even numbers.
        if x % 2 == 0 and y % 2 == 0:
            # If both 'x' and 'y' are even, call the original function 'f' with arguments 'x' and 'y'.
            f(x, y)
        else:
            # If either 'x' or 'y' is not even, print a message indicating that both numbers should be even.
            print("Enter even numbers.")
    # Return the inner function.
    return inner

# Define a function 'add' that takes two arguments 'a' and 'b'.
@extra_add  # Apply the 'extra_add' decorator to the 'add' function.
def add(a, b):
    # Print the sum of 'a' and 'b'.
    print(a + b)

# Call the 'add' function with arguments 2 and 4.
add(2, 4)
