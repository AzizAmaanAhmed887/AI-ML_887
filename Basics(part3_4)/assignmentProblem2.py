# define list of type integer

integer_list = [3, 3]

length = len(integer_list)
for num in integer_list:
    allNum = num + allNum
    print(f"average = {allNum / length}")
