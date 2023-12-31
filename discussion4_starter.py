class Rectangle():
    # Create the constructor "__init__" method
    # Arguments: width (an ingeter), height (an integer)
    # 
    # It sets an instance variable, "width" to the passed argument, width
    # It sets an instance variable, "height" to the passed argument, height

    def __init__(self, width, height):
        self.width = width
        self.height = height



    # Create the "__str__" method
    #
    # It returns a string, 
    #       "A rectangle with width ____ and height ____"

    def __str__(self):
        return "A rectangle with width {0} and height {1}".format(self.width, self.height)



    # Create the "verify_input" method
    #
    # It returns a boolean
    #       True if the width and height are positive numbers
    #       False otherwise

    def verify_input(self):
        return self.width > 0 and self.height > 0



    # Create the "area" method
    #
    # It first verifies inputs and return "Invalid input" if they are invalid.
    # Otherwise, it returns the area of the rectangle.

    def area(self):
        if verify_input(self):
            return self.height * self.width
        else:
            return "Invalid input"



    # Create the "perimeter" method
    #
    # It first verifies inputs and return "Invalid input" if they are invalid.
    # Otherwise, it returns the perimeter of the rectangle.

    def perimeter(self):
        if verify_input(self):
            return (self.width + self.height)*2
        else:
            return "Invalid input"
    


def main():
    r = Rectangle(10, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

    r = Rectangle(0, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

if __name__ == "__main__":
    main()