class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)


def main():
    try:
        __a = int(input("Enter A "))
        __b = int(input("Enter b "))
        rectangle = Rectangle(__a, __b)
        print(f"Area of rectangle: {rectangle.area()}")
        print(f"Perimeter of rectangle: {rectangle.perimeter()}")

    except ValueError:
        print("Invalid input!")


if __name__ == '__main__':
    main()
