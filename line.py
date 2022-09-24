import pyglet
from pyglet.math import *

from point import *

class Wood:
    # connects two points/pivots with wood
    def __init__(self, a, b, length=None, batch=None):
        # points / pivots
        self.a = a
        self.b = b

        self.shape = pyglet.shapes.Line(self.a.x.x, self.a.x.y,
                                        self.b.x.x, self.b.x.y,
                                        color=(110, 95, 70), width=4,
                                        batch=batch)

        if length is not None:
            self.l = length
        else:
            self.l = self.a.x.distance(self.b.x)

    def update(self, dt):
        c = (self.a.x + self.b.x).scale(0.5)
        d = (self.a.x - self.b.x).normalize()

        if type(self.a) == Point:
            self.a.x = c + d.scale(self.l / 2)

        if type(self.b) == Point:
            self.b.x = c - d.scale(self.l / 2)

        self.shape.position = *self.a.x, *self.b.x


class Spring(Wood):
    def __init__(self, a, b, length=None, k=1, batch=None):
        # points / pivots
        self.a = a
        self.b = b
        self.k = k

        self.shape = pyglet.shapes.Line(self.a.x.x, self.a.x.y,
                                        self.b.x.x, self.b.x.y,
                                        color=(220, 200, 30), width=3,
                                        batch=batch)

        if length is not None:
            self.l = length
        else:
            self.l = self.a.x.distance(self.b.x)

    def update(self, dt):
        d = self.a.x.distance(self.b.x)
        n = (self.a.x - self.b.x).normalize()
        factor = 0.5 if type(self.a) == type(self.b) == Point else 1

        self.a.apply_forces(n.scale(-self.k * (d - self.l)))
        self.b.apply_forces(n.scale(self.k * (d - self.l)))


        self.shape.position = *self.a.x, *self.b.x
