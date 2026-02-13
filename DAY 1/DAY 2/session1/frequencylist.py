numbers = input("Enter numbers separated by space: ")
num_list = numbers.split()

for i in num_list:
    count = num_list.count(i)
    if count > 2:
        print(i, "appears", count, "times")
