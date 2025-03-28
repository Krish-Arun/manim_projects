from manim import *
from sympy import *

x=symbols('x')
expr=cos(x)
ord=10

def taylor_term (expr,ord):
    return ((x**ord)*(diff(expr,x,ord).subs(x,0)))/factorial(ord) 

def taylor_series(expr,ord):
    return sum([taylor_term(expr,i) for i in range(0,ord+1,2)])


class Taylor(Scene):
    def construct(self):
        axes = Axes(x_range=[-10, 10, 1], y_range=[-2,2,0.5])
        axes.to_edge(DOWN)

        text0=Text("Let's start from cos(0)")
        text0.to_edge(UP)

        graph0=axes.plot(lambda x: cos(x), color=BLUE)
        self.add(axes,graph0)

        graph1_1=(axes.plot(lambda x: 1, color=PURPLE_A, x_range=[0, 0]))
        graph1_2=(axes.plot(lambda x: 1, color=PURPLE_A, x_range=[-6, 6]))
        
        self.play(
            Write(text0),
            Transform(graph1_1,graph1_2),
            run_time=3
        )
        self.remove(graph1_1)
        self.remove(graph1_2)
        self.remove(text0)


        for order in range(2,ord+1,2):

            text1=Text("add  "+str(taylor_term(expr,order)),font_size=32)
            text1.to_edge(UP)

            graph_i=axes.plot(lambda u: (taylor_series(expr,order-2)).subs(x,u), color=PURPLE_A, x_range=[-6, 6])
            graph_f=axes.plot(lambda u: (taylor_series(expr,order)).subs(x,u), color=PURPLE_A, x_range=[-6, 6])

            self.add(axes,graph_i)
            
            self.play(
                Write(text1),
                run_time=2
            )
            self.play(
                Transform(graph_i,graph_f),
                run_time=4
            )
            self.remove(graph_i)
            self.remove(text1)

        