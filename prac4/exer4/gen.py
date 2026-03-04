# 1. Generator for squares up to N
def square_gen(n):
    for i in range(n + 1):
        yield i ** 2

# 2. Print even numbers up to n comma-separated
def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield str(i) 

n = int(input())
print(",".join(even_generator(n)))
        

# 3. Generator for numbers divisible by 3 and 4 up to n
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# 4. Generator squares from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a, b = map(int, input().split())
for s in squares(a, b):
    print(s)

# 5. Generator from n down to 0
def countdown(n):
    for i in range(n, -1, -1):
        yield i