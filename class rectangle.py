class Rectangle:

    def CalculateArea(self):
#this function will accept input of length and breadth and calculate area
        self.width=int(input("Enter Length:"))
        self.height=int(input("Enter breadth:"))
        area=self.width*self.height
        print(area)
        return (area)


    def CalculatePerimeter(self):
#this function will accept input and calculate perimeter
        perimeter=2*(self.width+self.height)
        print(perimeter)
        return (perimeter)

    

class Square:

    def CalculateArea(self):
#this function will accept input side and calculate area
        print("Enter side:")
        self.s=float(input())
        area=self.s*self.s
        return(area)

    def CalculatePerimeter(self):
#this function will accept input and calculate perimeter
        perimeter=4*self.s
        return(perimeter)

#calling the functions
c=Square()
x=c.CalculateArea()
y=c.CalculatePerimeter()
print("Area of square is=%f"%(x))
print("perimeter of square is=%f"%(y))

c=Rectangle()
x=c.CalculateArea()
y=c.CalculatePerimeter()
print("Area of rectangle is=%f"%(x))
print("Perimeter of rectangle is=%f"%(y))
