import json

# using dump()
data = {"name": "Sharon", "city": "Bhopal"}
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
print("Data dumped successfully")
# using load()
with open("data.json", "r") as f:
    data = json.load(f)
print(data)

# using loads()
json_data = '{"name": "Amaan", "age": 21}'
python_obj = json.loads(json_data)
print(python_obj["name"])

# using dumps()

data = {
    "name": "Amaan",
    "age":25,
    # "marks": [85, 90, 92],
    "isIntern":True
}
json_string = json.dumps(data)
print(json_string)
