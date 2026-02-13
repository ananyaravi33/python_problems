list_of_IDs = input("Enter the List of ID:").split()
Initial_set=set(list_of_IDs)

duplicate_set=set()
for product in list_of_IDs:
    if list_of_IDs.count(product)>1:
        duplicate_set.add(product)
print("Duplicate IDs:", duplicate_set)

