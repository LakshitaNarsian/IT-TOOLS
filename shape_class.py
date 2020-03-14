# Defining Base class 'Shape'  
class Shape:

    
    def _get_Length_Breadth(self):
         # Function to initialize the Data Members
        self._length = int(input("Enter Length: "))
        self._breadth = int(input("Enter Breadth: "))


# Defining Derived class 'Rectangle'  
class Rectangle(Shape):

    
    def calculate_area(self):
        # Function to calculate area of rectangle 
        print("Area of Rectangle is ", self._length * self._breadth)


# Creating Object 
obj = Rectangle()
# Calling function to get input
obj._get_Length_Breadth()
# Calling function to get the area of rectangle
obj.calculate_area()
