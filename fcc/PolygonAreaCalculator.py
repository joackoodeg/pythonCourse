class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def set_width(self,width):
        self.width=width
    
    def set_height(self,height):
        self.height=height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2*self.width + 2*self.height
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        if self.width > 50 or self.height> 50:
            return "Too big for picture."  
        else:
            rectangle = ''
            for _ in range(self.height):
                rectangle += '*' * self.width + '\n'
        return rectangle
    
    def get_amount_inside(self, other):
        return self.get_area() // other.get_area()
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self,length):
        self.width = length
        self.height = length

    def set_side(self, length):
        self.width = length
        self.height = length

    def set_width(self, width):
        super().set_width(width)
        super().set_height(width)

    def set_height(self, height):
        super().set_width(height)
        super().set_height(height)

    def __str__(self):
        return f"Square(side={self.width})"

if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))