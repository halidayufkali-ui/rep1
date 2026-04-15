from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map()
squared = list(map(lambda x: x**2, numbers))
print("Squared:", squared)

# filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)

# reduce()
sum_all = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce:", sum_all)