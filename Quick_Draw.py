
from quickdraw import QuickDrawData
import quickdraw
import svgwrite

def normalize_strokes(strokes, size):
    min_x, min_y, max_x, max_y = float('inf'), float('inf'), float('-inf'), float('-inf')
    
    for stroke in strokes:
        for coordinate in stroke:
            x, y = coordinate
            min_x, min_y = min(min_x, x), min(min_y, y)
            max_x, max_y = max(max_x, x), max(max_y, y)
            
    scale_x, scale_y = (size / (max_x - min_x)), (size / (max_y - min_y))
    scale = min(scale_x, scale_y)
    
    normalized_strokes = []
    for stroke in strokes:
        new_stroke = [(scale * (x - min_x), scale * (y - min_y)) for x, y in stroke]
        normalized_strokes.append(new_stroke)
    
    return normalized_strokes

qd = quickdraw.QuickDrawData()
image_size = 255
padding = 50
columns = 15
rows = 20
total_images = columns * rows
grid_width = (image_size + padding) * columns
grid_height = (image_size + padding) * rows

dwg = svgwrite.Drawing('coffee_cup_grid.svg', profile='tiny', size=(grid_width, grid_height))

for i in range(total_images):
    coffee_cup = qd.get_drawing("coffee cup")  # Fetch a new coffee cup each time
    normalized_strokes = normalize_strokes(coffee_cup.strokes, image_size)
    
    row = i // columns
    col = i % columns
    x_offset = col * (image_size + padding)
    y_offset = row * (image_size + padding)

    for stroke in normalized_strokes:
        points = []
        for coordinate in range(len(stroke)):
            x = stroke[coordinate][0] + x_offset
            y = stroke[coordinate][1] + y_offset
            points.append((x, y))
        dwg.add(dwg.polyline(points, stroke=svgwrite.rgb(0, 0, 0), stroke_width=2, fill='none'))

dwg.save()