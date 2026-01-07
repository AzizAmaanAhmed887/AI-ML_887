# squares = []
#
# for i in range(1, 6):
#     squares.append(i * i)
# print(f"without list comprehension output = {squares}")

squares = [i * i for i in range(1, 6)]
print(f"list comprehension output = {squares}")
