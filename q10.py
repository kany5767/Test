def draw_triangle(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

height = int(input("Enter Number: "))
draw_triangle(height)