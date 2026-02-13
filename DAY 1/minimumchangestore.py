amount = int(input("Enter the change mount: "))
print(type(amount))
c100 = amount//100
amount = amount%100
c50 = amount//50
amount = amount%50
c20 = amount//20
amount = amount%20
c10 = amount//10
amount = amount%10
c5 = amount//5
amount = amount%5
c2 = amount//2
amount = amount%2
c1 = amount
total_amount = c100+c50+c20+c10+c5+c2+c1
print("total change amount = ",total_amount)


