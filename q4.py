def draw_inverted_triangle(height):
    for i in range(height, 0, -1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

height = int(input("ใส่ตัวเลขที่ต้องการ: "))
draw_inverted_triangle(height)