# presets for things
from point import *
from line import *

def brigde_1(pb, lb):
    points = [
        Pivot(200, 300, batch=pb),
            Point(250, 350, batch=pb),
        Point(300, 300, batch=pb),
            Point(350, 350, batch=pb),
        Point(400, 300, batch=pb),
            Point(450, 350, batch=pb),
        Point(500, 300, batch=pb),
            Point(550, 350, batch=pb),
        Point(600, 300, batch=pb),
            Point(650, 350, batch=pb),
        Pivot(700, 300, batch=pb),
    ]

    lines = []
    for i in range(len(points) - 1):
        lines.append(Wood(points[i], points[i + 1], batch=lb))

    for i in range(0, len(points) - 2, 2):
        lines.append(Wood(points[i], points[i + 2], batch=lb))

    for i in range(1, len(points) - 3, 2):
        lines.append(Spring(points[i], points[i + 2], k=0.5, batch=lb))

    return (points, lines)
