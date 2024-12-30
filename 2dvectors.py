from reusabletools import create_canvas, draw_line, draw_point

def print_canvas(canvas):
    for row in canvas:
        print(''.join(row))

def add_axis(canvas):
    center = len(canvas) // 2
    for i in range(len(canvas[0])):
        canvas[center][i] = '-'
    for i in range(len(canvas)):
        canvas[i][center] = '|'
    canvas[center][center] = '+'

def draw_vector(canvas, x1, y1, x2, y2):
    print(f"Drawing vector from ({x1},{y1}) to ({x2},{y2})")  # Debug
    draw_line(canvas, x1, y1, x2, y2)
    
def draw_polygon(canvas, points):
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        draw_line(canvas, x1, y1, x2, y2)

def main():
    print("Creating canvas...")
    canvas = create_canvas(15, 15)
    
    print("Adding axis...")
    add_axis(canvas)
    
    print("Drawing vectors...")
    vectors = [(0, 0, 3, 4), (0, 0, 5, -3)]
    for vector in vectors:
        draw_vector(canvas, *vector)
    
    print("Drawing polygon...")
    polygon_points = [(0, 0), (3, 4), (5, -3)]
    draw_polygon(canvas, polygon_points)
    
    print("Final canvas:")
    print_canvas(canvas)

if __name__ == "__main__":
    main()
