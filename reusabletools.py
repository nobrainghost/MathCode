def create_canvas(width, height):
    return [[' ' for _ in range(width)] for _ in range(height)]

def print_canvas(canvas):
    for row in canvas:
        print(''.join(row))

def draw_point(canvas, x, y):
    height = len(canvas)
    width = len(canvas[0])
    center_x = width // 2
    center_y = height // 2
    
    # Transform coordinates
    canvas_x = center_x + x
    canvas_y = center_y - y  # Flip y-axis
    
    # Bounds checking
    if 0 <= canvas_x < width and 0 <= canvas_y < height:
        canvas[canvas_y][canvas_x] = '*'

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
