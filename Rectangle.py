class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {"length": self.length}
        yield {"width": self.width}


# Creating a Rectangle instance
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
rect = Rectangle(length, breadth)

# Iterating over the rectangle
for ele in rect:
    print(ele)
