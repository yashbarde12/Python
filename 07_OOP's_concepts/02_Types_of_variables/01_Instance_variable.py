# Types of variables:
'''
1. Instance variable (Object level variables)
2. Static variable (Class level variables)
3. Local variable (Method level variables)  '''
#--------------------------------------------------------
# Instance Variable 
'''
- Varibale who's value changes from object to object called as instance variable.
- Where to declare, access, update instance variable :
        1. inside a class:
            - in instance method and constructor by using self.
            - instance method's variable get added to the memory only after calling that instance method.
        2. outside a class:
            - using reference variable.
- Example:
        class MyClass: 
            def init(self, var):
                self.instance_var = var
'''
#--------------------------------------------------------
print("----- Example 1-----")

class Demo:
    def im_instance_method(self):
       self.a = 30  # Creating instance variable in instance method using self
       self.b = 40  # Creating instance variable in instance method using self
       print("getting value of d from constructor:",self.d) # Accessing instance variable
       self.d = 69852 # Updating instance variable
       print("after updating value of d from constructor:",self.d)
       del self.d # Deleting instance variable
       #print("after deleting value of d from constructor:",self.d) ERROR
       
    def __init__(self):
       self.c = 11  # Creating instance variable in constructor using self
       self.d = 22  # Creating instance variable in constructor using self
       
d1 = Demo()

d1.e = 5  # Creating instance variable in outside a class using reference variable

# print(d1.a) # AttributeError: 'Demo' object has no attribute 'a'
# print(d1.b) # AttributeError: 'Demo' object has no attribute 'b'
# getting error for a and b because im_instance_method() is not called yet
print(d1.c) # 11
print(d1.d) # 22
print(d1.e) # 5

d1.im_instance_method()
''' Output:
    getting value of d from constructor: 22
    after updating value of d from constructor: 69852'''
print(d1.a) # 30
print(d1.b) # 40
#--------------------------------------------------------
print("----- Example 2-----")

class Phone:
    def __init__(self, brand, price, chargerType):
        self.brand = brand
        self.price = price
        self.chargerType = chargerType
 
    def display(self):
        print("Brand : ", self.brand)
        print("Price : ", self.price)
        print("Charger Type : ", self.chargerType)

samsung = Phone("Samsung", 45000, "Type-C")
samsung.display()
''' Output:
Brand :  Samsung
Price :  45000
Charger Type :  Type-C '''
#--------------------------------------------------------
#--------------------------------------------------------