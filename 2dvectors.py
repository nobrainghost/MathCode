#Simulating a Cartesian Plane
def create_canvas(width, height):
    return[[' ' for i in range(width)] for j in range(height)]
def print_canvas(canvas):
    for row in canvas:
        print(''.join(row))

def draw_point(canvas,x,y):
    canvas[y][x] = '*'

canvas=create_canvas(10,10)
draw_point(canvas,5,5)
print_canvas(canvas)