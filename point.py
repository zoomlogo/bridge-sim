import pyglet
from pyglet.math import *

class Pivot:
    # the pivot is fixed in position
    def __init__(self, x, y, batch=None):
        self.x = Vec2(x, y)
        self.v = Vec2()
        self.a = Vec2()
        self.shape = pyglet.shapes.Rectangle(x - 5, y - 5, 10, 10, color=(250, 80, 120), batch=batch)

    def update(self, dt):
        # can't update a fixed point, can we?
        pass

    def apply_forces(self, *forces):
        self.a = sum(forces) # / 1 as mass is 1

    def draw(self):
        self.shape.draw()


class Point(Pivot):
    # point ain't fixed
    def __init__(self, x, y, batch=None):
        self.x = Vec2(x, y)
        self.v = Vec2()
        self.a = Vec2()
        self.px = self.x
        self.shape = pyglet.shapes.Circle(self.x.x, self.x.y, 7, color=(20, 20, 20), batch=batch)

    def update(self, dt):
        _px = self.x
        self.x = self.x + (self.x - self.px)
        self.v = self.a.scale(dt)
        self.x = self.x + Vec2(0, -10).scale(dt * dt) + self.v.scale(dt)
        self.a = Vec2()
        self.px = _px

        self.shape.position = self.x

