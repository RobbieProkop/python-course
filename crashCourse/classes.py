# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#  Create class
class User:
  # constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    
  #create method
  def greeting(self):
    return f"My name is {self.name}, and I am {self.age}" 

  def has_birthday(self):
    self.age += 1
    
    
    
# extend class
class Customer(User):
  # Customer
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0

  # set balance
  def set_balance(self, balance):
    self.balance = balance
  
  def greeting(self):
    return f"My name is {self.name}, I am {self.age} and my balance is {self.balance}" 
  
# init user object
robbie = User('Robbie', "a@b.ca", 28)

robbie.has_birthday()

# init customer
cust1 = Customer("Janet", 'janet@jan.ca', 36)

cust1.set_balance(1500)
print(cust1.greeting())


# print(robbie.greeting())
