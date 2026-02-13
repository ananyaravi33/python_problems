number = input("Enter number plate number: ")

same = True
ascending = True
descending = True

for i in range(len(number) - 1):
    if number[i] != number[i + 1]:
        same = False
    if number[i] >= number[i + 1]:
        ascending = False
    if number[i] <= number[i + 1]:
        descending = False

if not same and not ascending and not descending:
    print("Fancy Number")
else:
    print("Not a Fancy Number")
