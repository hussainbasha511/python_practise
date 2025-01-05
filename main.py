# prime numbers
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Palindrome
def is_palindrome(string):
    cleaned_string = ''.join(string.split()).lower()
    return cleaned_string == cleaned_string[::-1]

# Fibonacci
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Arm strong
def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == num

# Sum of digits

def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

# Printing string in reverse order

def reverse_string(string):
    return string[::-1]

# list of colors printing in ascending or descending order
def sort_colors(colors, order="ascending"):
    if order == "ascending":
        return sorted(colors)  # Sort in ascending order
    elif order == "descending":
        return sorted(colors, reverse=True)
