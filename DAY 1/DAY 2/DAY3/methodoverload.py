# Parent Class
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Child Class
class Dog(Animal):
    def sound(self):   # Overriding parent method
        print("Dog barks")

# Another Child Class
class Cat(Animal):
    def sound(self):   # Overriding parent method
        print("Cat meows")


# Creating objects
a = Animal()
d = Dog()
c = Cat()

# Calling methods
a.sound()
d.sound()
c.sound()
