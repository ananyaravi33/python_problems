class A:
    def show(self):
        print(" ShowingConstructor A")

class B:
    def show(self):
        print(" showing Constructor B")

class C(A, B):
    pass
        
       
obj = C()
obj.show()