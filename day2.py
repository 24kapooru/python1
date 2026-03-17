#multiplications
print("Multiplication Tables 1-10")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()

print("\n" + "-"*40 + "\n")

print("Multiplication Tables 11-20")
for i in range(11, 21):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()

#fibonacci
def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print(f"Fibonacci: {fibonacci(10)}")

#armstrong no.
def is_armstrong(num):
    order = len(str(num))
    temp = num
    sum_val = 0
    
    while temp > 0:
        digit = temp % 10
        sum_val += digit ** order
        temp //= 10
        
    return num == sum_val

print(f"Is 153 Armstrong? {is_armstrong(153)}")

#prime no.
def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"Is 17 prime? {is_prime(17)}")

#palidrome no. or string
def is_palindrome(data):
    
    clean_data = str(data).lower().replace(" ", "")
    return clean_data == clean_data[::-1]

print(f"Is 'Racecar' a palindrome? {is_palindrome('Racecar')}")
print(f"Is 121 a palindrome? {is_palindrome(121)}")