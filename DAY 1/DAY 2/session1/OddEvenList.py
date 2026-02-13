numbers = input("Enter numbers : ")
num_list = numbers.split()

even = 0
odd = 0

for i in num_list:
    n = int(i)
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Number of even numbers:", even)
print("Number of odd numbers:", odd)

