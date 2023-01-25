def rectangle(length, width):
    def rectangle_area():
        return length * width

    def rectangle_perimeter():
        return (length * 2) + (width * 2)

    if type(length) != int or type(width) != int:
        return "Enter valid values!"

    return f'''Rectangle area: {rectangle_area()}
Rectangle perimeter: {rectangle_perimeter()}'''

print(rectangle(2, 10))