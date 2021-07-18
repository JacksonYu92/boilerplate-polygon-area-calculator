class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width
        return

    def set_height(self, height):
        self.height = height
        return

    # get_area: Returns area (width * height)
    def get_area(self):
        area = self.width * self.height
        return area

    # get_perimeter: Returns perimeter (2 * width + 2 * height)
    def get_perimeter(self):
        perimeter = (self.width + self.height) * 2
        return perimeter

    # get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        if (self.width > 50 or self.height > 50):
            return "Too big for picture."
        string = (("*" * self.width) + "\n") * self.height
        return string


    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())




class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return "Square(side={})".format(self.width)

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)
