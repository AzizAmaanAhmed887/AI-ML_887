l = [10, 20, 30, 40, 50, 60]
x = 40
idx = 0

for i in l:
    if i == x:
        print(f"{x} is at index = {idx}")
        break
    idx += 1