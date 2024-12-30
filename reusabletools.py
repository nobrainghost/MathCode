# Simulating a Cartesian Plane
def create_canvas(width, height):
    return [[' ' for _ in range(width)] for _ in range(height)]

def print_canvas(canvas):
    for row in canvas:
        print(''.join(row))

def draw_point(canvas, x, y):
    center_x = len(canvas) // 2
    center_y = len(canvas[0]) // 2
    canvas[center_x - x][center_y + y] = '*'

def add_axis(canvas):
    center_x = len(canvas) // 2
    center_y = len(canvas[0]) // 2

    for i in range(len(canvas)):
        canvas[i][center_y] = '|'

    for i in range(len(canvas[0])):
        canvas[center_x][i] = '-'
    canvas[center_x][center_y] = '0'

canvas = create_canvas(11, 11)  # Create a canvas with odd dimensions
add_axis(canvas)

# Draw points
draw_point(canvas, 0, 5)  # Point at (0, 5)
draw_point(canvas, 2, -3)  # Point at (2, -3)
draw_point(canvas, -4, -2)  # Point at (-4, -2)

# Print the canvas
print_canvas(canvas)
