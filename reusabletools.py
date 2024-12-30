def create_canvas(width, height):
    return [[' ' for _ in range(width)] for _ in range(height)]

def print_canvas(canvas):
    for row in canvas:
        print(''.join(row))

def draw_point(canvas, x, y):
    center_x = len(canvas) // 2
    center_y = len(canvas[0]) // 2
    canvas_x = center_x - x
    canvas_y = center_y + y
    if 0 <= canvas_x < len(canvas) and 0 <= canvas_y < len(canvas[0]):
        canvas[canvas_x][canvas_y] = '*'

def add_axis(canvas):
    center_x = len(canvas) // 2
    center_y = len(canvas[0]) // 2
    for i in range(len(canvas)):
        canvas[i][center_y] = '|'
    for i in range(len(canvas[0])):
        canvas[center_x][i] = '-'
    canvas[center_x][center_y] = '0'

def draw_line(canvas, x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    
    while True:
        draw_point(canvas, x1, y1)
        
        if x1 == x2 and y1 == y2:
            break
        
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

# canvas = create_canvas(11, 11)
# add_axis(canvas)
# draw_line(canvas, 0, 0, 10, 10)
# print_canvas(canvas)
