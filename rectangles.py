# DO NOT ALLOW FOR CHARACTERS TO BE OUT OF BOUNDS

class Canvas: 
    
    canvas = []

    def print_canvas(self):
        for item in self.canvas: 
            print(item)

    def clear_canvas(self):
        self.canvas = []

    def add_rectangle(self, Rectangle):
        x_min = min(Rectangle.start_x, Rectangle.end_x)
        y_min = min(Rectangle.start_y, Rectangle.end_y)

        x_max = max(Rectangle.start_x, Rectangle.end_x)
        y_max = max(Rectangle.start_y, Rectangle.end_y)

        rectangle_string = ''
        for i in range(9):
            if x_min <= i <= x_max:
                rectangle_string += Rectangle.fill_char
            else:
                rectangle_string += " "

        for i in range(9):
            if y_min <= i <= y_max:
                self.canvas.append(rectangle_string)
            else:
                self.canvas.append(' ')
    #method to clear
    #set the bounds to be 10x10 

class Rectangle:
  
    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.fill_char = fill_char

    def char(self, fill_char):
        self.fill_char = fill_char
    
    def translate(self, axis, num):
        """Translate the rectangle, axis can either be 'x' or 'y'
        Translating on x will move it left or right,
        tranlating on y will move it up or down."""

        pass
        
    def __repr__(self):
        return f'<Rectangle start=({self.start_x}, {self.start_y}) end=({self.end_x}, {self.end_y}) fill_char={self.fill_char}>'
    #attribute for fill_char 
    #method to print the rectangle to a canvas? 

#need to handle translating the rectangle 

canvas1 = Canvas()
canvas1.print_canvas()
rectangle1 = Rectangle(5,4,3,2,".")
print("*****")
canvas1.add_rectangle(rectangle1)
canvas1.print_canvas()
print("*****")
rectange2 = Rectangle(7,8,5,6,"+")
canvas1.add_rectangle(rectange2)
canvas1.print_canvas()
