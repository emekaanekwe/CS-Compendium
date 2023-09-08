class Fib:
    def __init__(self):
        # memoization.
        self.memo = {}
    def calculate(self, n):
        # Check if the result for 'n' has already been calculated and cached.
        if n in self.memo:
            return self.memo[n]
        # Base cases
        if n == 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = self.calculate(n - 1) + self.calculate(n - 2)
        # Cache the result for future use.
        self.memo[n] = result
        return result

fibonacci_calculator = Fib()
n = 10 
result = fibonacci_calculator.calculate(n)
print(f"The {n}-th Fibonacci number is: {result}")