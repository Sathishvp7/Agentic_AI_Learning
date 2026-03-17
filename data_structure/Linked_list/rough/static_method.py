""""
What is @staticmethod?

A static method is a method inside a class that:

❌ Does NOT use self

❌ Does NOT access instance variables

❌ Does NOT access class variables

✅ Just logically belongs to the class

It behaves like a normal function, but grouped inside a class for organization.

"""

# Simple Example – Without @staticmethod
class MathUtils:

    def add(self, a, b):
        return a + b
    
obj = MathUtils()
print(obj.add(5, 3)) # output = 8

# Problem  We had to create an object(obj = MathUtils()) just to add two numbers.

# Same Example – With @staticmethod
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

# output = 8 -->No object creation needed,Cleaner,Used like a utility function
print(MathUtils.add(5, 3))