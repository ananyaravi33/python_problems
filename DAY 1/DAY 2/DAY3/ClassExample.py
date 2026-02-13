class Mobile:

    # Constructor
    def __init__(self, brand=None, model=None, price=None):
        if brand is None and model is None and price is None:
            print("Default Constructor Called")
        else:
            self.brand = brand
            self.model = model
            self.price = price

    # Method to display details
    def display(self):
        if hasattr(self, "brand"):
            print("Brand:", self.brand)
            print("Model:", self.model)
            print("Price:", self.price)
        else:
            print("No mobile details available.")


# Example 1: Default Constructor
m1 = Mobile()
m1.display()

print("-------------------")

# Example 2: Parameterized Constructor
m2 = Mobile("Samsung", "S23", 80000)
m2.display()
