name = input("Enter the name: ")

# remove spaces
name = name.replace(" ", "")

mid = len(name) // 2

firstHalf = name[:mid]
secondHalf = name[mid:]

rev_firstHalf = firstHalf[::-1]
rev_secondHalf = secondHalf[::-1]

result = rev_secondHalf + rev_firstHalf

print(result)
