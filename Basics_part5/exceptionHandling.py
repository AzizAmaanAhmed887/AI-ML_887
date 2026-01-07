# try, except, else, finally

try:
    n = int(input("Enter a number: "))
    print(10 / n)

except ZeroDivisionError:
    print("Division by zero is not allowed")

except ValueError:
    print("Invalid value")

else:
    print("Execution successfully")

finally:
    print("program finished 👌")