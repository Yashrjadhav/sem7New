recursive_step_count = 0
iterative_step_count = 0

def fibonacci_recursive(n):
    global recursive_step_count
    recursive_step_count += 1

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    global iterative_step_count
    iterative_step_count += 1  

    if n <= 0:
        return 0 ,[0]
    elif n == 1:
        return 1 ,[0,1]

    a, b = 0, 1
    sequence = [0, 1] 

    for _ in range(2, n + 1):
        iterative_step_count += 1
        a, b = b, a + b
        sequence.append(b)

    return b, sequence


n = int(input("Enter a number: "))

fib_recursive = fibonacci_recursive(n)
print(f"Fibonacci number (Recursive) for n = {n}: {fib_recursive}")
print(f"Number of steps (Recursive) to calculate Fibonacci number for n = {n}: {recursive_step_count}")

fib_iterative, fib_sequence = fibonacci_iterative(n)
print(f"Fibonacci number (Iterative) for n = {n}: {fib_iterative}")
print(f"Fibonacci sequence up to position {n}: {fib_sequence}")
print(f"Number of steps (Iterative) to calculate Fibonacci number for n = {n}: {iterative_step_count}")
