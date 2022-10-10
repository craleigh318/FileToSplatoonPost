# Created by Christopher Raleigh


import argparse
from PIL import Image


WIDTH = 320
HEIGHT = 120


def file_to_image(filename):
    image = Image.open(filename)
    converted = image.convert('1')
    data = converted.getdata()
    return list(data)


def is_black(image, x, y):
    i = WIDTH * y + x
    pixel = image[i]
    return pixel == 0


def create_output(image):
    reverse = False
    x = 0
    y = 0
    output = ''
    while y < HEIGHT:
        black = is_black(image, x, y)
        if black:
            output += 'a\n'
        move_down = False
        if reverse:
            if x <= 0:
                move_down = True
            else:
                x -= 1
                output += 'left\n'
        else:
            if x >= WIDTH - 1:
                move_down = True
            else:
                x += 1
                output += 'right\n'
        if move_down:
            y += 1
            reverse = not reverse
            output += 'down\n'
    return output


def paint(image, output_filename):
    output = create_output(image)
    with open(output_filename, 'w') as f:
        print(output, file=f)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--i', type=str, required=True)
    parser.add_argument('--o', type=str, required=True)
    args = parser.parse_args()
    input_filename = args.i
    image = file_to_image(input_filename)
    output_filename = args.o
    paint(image, output_filename)


if __name__ == '__main__':
    main()
