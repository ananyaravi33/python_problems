tuple_list=eval(input("Enter the list of tuples"))
k=int(input("Enter the k value"))

product=1
for tup in tuple_list:
    if k<<len(tup):
        product = product*tup[k]
    else:
        print("Invalid k value")
        break
