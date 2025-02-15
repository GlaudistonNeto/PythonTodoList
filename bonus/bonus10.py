try:
    width = float(input('Enter the rectangle width: '))
    length = float(input('Enter the rectangle length: '))

    if width == length:
        exit("It shouldn't be a square area calculation")

    area = width * length
    print(area)
except ValueError:
    print("It's expected numbers to be multiplied" )