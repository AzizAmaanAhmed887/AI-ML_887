nums = [-2, -4, 3, 5, 2, -1]
# list comprehension for all -ve values -> 0
nums = [0 if val < 0 else val for val in nums]
print(nums)

# Using methods in list comprehension
words = ["python", "java", "c++"]
print(words)
words = [val.upper() for val in words]
print(words)

# using list comprehension in numbers
squares = []
for i in range(1, 6):
    squares.append(i * i)
print(f"without list comprehension output = {squares}")

# list comprehension with condition
squares = [i * i for i in range(1, 6) if i % 2 == 0]
print(f"list comprehension output = {squares}")
