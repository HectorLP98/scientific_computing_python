class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2*self.width + 2*self.height
    
    def get_diagonal(self):
        return (self.width **2 + self.height**2) **0.5
    
    def get_picture(self):
        if self.height<50 and self.width <50:
            chart =''
            
            for k in range(self.height):
                chart += ''.center(self.width,'*') + '\n'
            return chart
        else:
            return "Too big for picture."
        
    def get_amount_inside(self,objeto):
        return self.get_area() // objeto.get_area()
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

# Herencia
class Square(Rectangle):
    
    def __init__(self, lado):
        self.height = lado
        self.width = lado
        
    def __str__(self):
        return f'Square(side={self.width})'
    
    def set_side(self, side):
        self.height = self.width = side
