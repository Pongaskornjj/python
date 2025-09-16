"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle():
    def __init__(self, width, length):
        self.__width = width
        self.__length = length
    
    def getArea(self):
        area = self.__width * self.__length
        return f"Area = {area}"
    
    def getPerimeter(self):
        perimeter = (self.__width + self.__length) * 2
        return f"Perimeter = {perimeter}"
    
    def isSquare(self):
        if self.__width == self.__length:
            return True
        else:
            return False
myRectangle = Rectangle(10,5)

print(myRectangle.getArea())
print(myRectangle.getPerimeter())
print(myRectangle.isSquare())