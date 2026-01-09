# open file in write mode
with open("names.txt", "w") as f:
    for i in range(5):
        names = input("Enter names: ")
        f.write(names + "\n")

# open file in read mode and print all names
with open("names.txt", "r") as f:
    file = f.readlines()
    for i in file:
        print(i)
