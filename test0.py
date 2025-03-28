
from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle() 
        square = Square()
        text1=Text("hey man")
        text1.to_edge(UP)
    

        square.to_corner(UR)
        # square.flip(RIGHT)
        
        numline = NumberLine()

        self.play(Write(text1,run_time=2))
        self.play(Create(square))
        self.play(Transform(square, circle))
        self.remove(square)
        self.play(Transform(circle,numline))
        self.remove(circle)
        self.add(numline)
        square.to_edge(DOWN)
        self.play(Transform(text1[4],square))
        
    