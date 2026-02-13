products = eval(input("Enter the dictionary of products and their prices: "))

choice = input("Sort by key or price? ").lower()
if choice == "key":
    sorted_dict = dict(sorted(products.items()))
    print("Sorted dictionary:", sorted_dict)
elif choice == "price":
    sorted_dict = dict(sorted(products.items(), key=lambda x: x[1]))
    print("Sorted by price:", sorted_dict)
else:
    print("Invalid choice")