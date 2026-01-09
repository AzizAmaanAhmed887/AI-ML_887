import json

cityDictionary = {
    "Austin": 10_000,
    "NYC":20_000,
    "Los Angeles":30_000,
}

with open("cities.json","w") as f:
    json.dump(cityDictionary,f, indent=4)

# cities and their population are
with open("cities.json","r") as f:
    data = json.load(f)

print("Cities and their population are: ")
for city, population in data.items():
    print(city+ ":" + str(population))

newCity = input("Enter City Name: ")
newPopulation = input("Enter Population Value: ")

# updating dictionary
cityDictionary[newCity] = int(newPopulation)
with open("cities.json","w") as f:
    json.dump(cityDictionary, f, indent=4)

print("\nJSON file updated successfully!")
