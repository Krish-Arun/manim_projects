from sympy import *
from manim import *

x=symbols('x')
y=cos(x)
order=8

def taylor_term (expr,ord):
    return ((x**ord)*(diff(expr,x,ord).subs(x,0)))/factorial(ord) 



class Taylor(Scene):
    def construct(self):
        
        text_final=Text("Taylor ["+str(y)+"] = "+" + ".join(["("+str(taylor_term(y,i))+")" for i in range(order+1) if (taylor_term(y,i))])+" ...",font_size=26)

        self.play(
            Write(text_final)
        )