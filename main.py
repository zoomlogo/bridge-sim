import pyglet
from pyglet.math import *

from point import *
from line import *

import setups

win = pyglet.window.Window(1024, 512, "Bridge Simulator")
pyglet.gl.glClearColor(0.4, 0.5, 0.8, 1)

pb = pyglet.graphics.Batch()
lb = pyglet.graphics.Batch()
points, lines = setups.brigde_1(pb, lb)

def update(dt):
    for point in points:
        point.update(dt)

    for line in lines:
        line.update(dt)

@win.event
def on_draw():
    win.clear()
    lb.draw()
    pb.draw()

pyglet.clock.schedule_interval(update, 1 / 60)
pyglet.app.run()
