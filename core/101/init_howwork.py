
# Set inside __init__
class MyClassA:
    def __init__(self):
        self.x = 10

objA = MyClassA()
print("objA.x value ", objA.x)

# Set inside other method
class MyClassB:
    def myinitilizer(self):
        self.x = 100

objB = MyClassB()
objB.myinitilizer()
print("objB.x value ", objB.x)


# Set from outside any method, no self
class MyClassC:
    pass

objC = MyClassC()
objC.x = 1000
print("objC.x value ", objC.x)

#objA.x = 10000
#print("objA.x value ", objA.x)


print(1,2,3,4,5, sep='*')
numbers = [1,2,3]
print(numbers)