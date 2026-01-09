# 1. Opens a file in append mode "log.txt"
# 2. Adds a new log entry (like "Program run successfully")
# 3. Opens the file in read mode and prints all logs

with open("log.txt", "a") as f:
    f.write("Logs added successfully" + "\n")  # a log

with open("log.txt", "r") as f:
    print("File logs: ")
    for i in f:
        print(i.strip())
