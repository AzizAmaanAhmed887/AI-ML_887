# with open("sample2.txt","w+") as f:
#     f.write("Prime ai/ml course ")
#     print(f.read())

#  delete a file
# import os
#
# if os.path.exists("sample.txt"):
#     os.remove("sample.txt")
#     print("File does exist and deleted successfully")
# else:
#     print("File not found")

word = "python"
data = True
line = 1

with open("sample.txt", "r") as f:
    while data:
        data = f.readline()

        if data in word:
            print(f"word {word} present in {line} line")
            break

        line += 1