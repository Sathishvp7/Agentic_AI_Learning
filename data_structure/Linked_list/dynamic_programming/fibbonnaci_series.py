"""
Dynamic Programming (DP) is a method used to solve problems by:

Breaking a problem into smaller subproblems, solving each subproblem once, storing the result, 
and reusing it when needed.

This helps avoid repeating the same calculations, making the program faster and more efficient."""

# Naive Recursive Approach (No Dynamic Programming)
"""
Naive Recursive Fibonacci
-------------------------
This approach directly follows the Fibonacci recurrence relation.
It recalculates the same values multiple times (overlapping subproblems).

This method directly uses the Fibonacci formula:
F(n)=F(n−1)+F(n−2)

"""

counter = 0

def fibonacci_recursive(n):
    global counter
    counter += 1
    
    if n == 0 or n == 1:
        return n
    
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


n = 35
result = fibonacci_recursive(n)

print("Naive Recursion")
print("Fibonacci(", n, ") =", result)
print("Function calls:", counter)


# Dynamic Programming – Top Down (Memoization)
"""
Dynamic Programming - Top Down (Memoization)
--------------------------------------------
Stores computed Fibonacci values to avoid recomputation.
Uses recursion + caching.

Concept - We store previously computed Fibonacci values in a dictionary (memo).
"""

memo = {}
counter_memo = 0

def fibonacci_memo(n):
    global counter_memo
    counter_memo += 1
    
    # Return cached result if available
    if n in memo:
        return memo[n]
    
    if n == 0 or n == 1:
        return n
    
    # Store result in memo dictionary
    memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    
    return memo[n]


n = 35
result = fibonacci_memo(n)

print("\nDynamic Programming (Top Down - Memoization)")
print("Fibonacci(", n, ") =", result)
print("Function calls:", counter_memo)

# Dynamic Programming – Bottom Up (Tabulation)

"""
Dynamic Programming - Bottom Up (Tabulation)
--------------------------------------------
Builds the Fibonacci sequence iteratively using a list.
Avoids recursion entirely.

Concept - Instead of recursion, we build the Fibonacci sequence step by step starting from the smallest values.
"""

counter_bottom_up = 0

def fibonacci_bottom_up(n):
    global counter_bottom_up
    
    fib_table = [0, 1]
    
    for i in range(2, n + 1):
        counter_bottom_up += 1
        fib_table.append(fib_table[i-1] + fib_table[i-2])
    
    return fib_table[n]


n = 35
result = fibonacci_bottom_up(n)

print("\nDynamic Programming (Bottom Up - Tabulation)")
print("Fibonacci(", n, ") =", result)
print("Iterations:", counter_bottom_up)

# Space Optimized Fibonacci (Best Version)
"""
Space Optimized Fibonacci
-------------------------
Uses only two variables instead of storing the full sequence.
Most efficient approach for Fibonacci.
"""

counter_optimized = 0

def fibonacci_optimized(n):
    global counter_optimized
    
    a, b = 0, 1
    
    for _ in range(n):
        counter_optimized += 1
        a, b = b, a + b
    
    return a


n = 35
result = fibonacci_optimized(n)

print("\nSpace Optimized Fibonacci")
print("Fibonacci(", n, ") =", result)
print("Iterations:", counter_optimized)