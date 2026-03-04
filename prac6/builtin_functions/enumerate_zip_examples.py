names = ["Ali", "Omar", "Sara"]
scores = [85, 90, 78]

# enumerate()
for index, name in enumerate(names):
    print(index, name)

# zip()
for name, score in zip(names, scores):
    print(name, score)

# sorted()
print("Sorted scores:", sorted(scores))

# len(), min(), max(), sum()
print("Length:", len(scores))
print("Min:", min(scores))
print("Max:", max(scores))
print("Sum:", sum(scores))