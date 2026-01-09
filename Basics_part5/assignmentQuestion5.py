import json

try:
    with open("data.txt", "r") as f:
        data = json.load(f)
        print(data)

except FileNotFoundError:
    print("File not found")