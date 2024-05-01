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
    return 2 * pow(e, -x)

class GraphFunctions(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-2, 6],
            y_range=[-2, 6],
            axis_config={"include_numbers": True}
        )

        f_graph = ax.plot(f, color=BLUE)
        f_text = MathTex(r"f(x)=e^x-1", color=BLUE).move_to(ax.coords_to_point(4, 4))

        g_graph = ax.plot(g, color=RED)
        g_text = MathTex(r"g(x)=2e^{-x}", color=RED).move_to(ax.coords_to_point(4, 3))

        self.play(Create(ax), runtime=2)
        self.play(Create(f_text), runtime=1)
        self.play(Create(f_graph), runtime=2)
        self.play(Create(g_text), runtime=1)
        self.play(Create(g_graph), runtime=2)
        # self.play(Create(f_graph), Create(g_graph), rumtime=3)


        dot = Dot().move_to(ax.coords_to_point(0.693, 1))
        coordinates = Text("(0.693, 1)").next_to(dot, RIGHT).scale(0.5)

        self.wait(1)
        self.play(Create(dot), runtime=1)
        self.wait(1)
        self.play(Write(coordinates), runtime=2)

        f_area = ax.get_area(f_graph, x_range=(0,0.693), color=BLUE, opacity=0.5)
        g_area = ax.get_area(g_graph, x_range=(0,0.693), color=RED, opacity=0.5)

        self.play(Create(f_area), runtime=2)
        self.play(Create(g_area), runtime=2)

        solutionText = MathTex(r"\int_0^{0.693}f(x)-g(x)dx=0.693", color=YELLOW).move_to(ax.coords_to_point(4, -2))
        self.wait(1)
        self.play(Write(solutionText), runtime=3)
        
        self.wait(5)

