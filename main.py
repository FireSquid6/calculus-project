from manim import *
from math import *

# class CreateCircle(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
#         self.play(Create(circle))  # show the circle on screen

def f(x):
    return pow(e, x) - 1

def g(x):
    return 2 * pow(e, -x) + 1

class GraphFunctions(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-2, 6],
            y_range=[-2, 6],
            axis_config={"include_numbers": True}
        )

        f_graph = ax.plot(f, color=BLUE)
        g_graph = ax.plot(g, color=RED)

        self.add(ax)

        self.play(Create(f_graph), Create(g_graph))

        self.wait(5)


