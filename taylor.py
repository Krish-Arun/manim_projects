from sympy import *

x=symbols('x')
y=sympify(input("enter the function you wish to expand:\t"))
order=int(input("enter the number of terms you wish to expand till:\t"))

def taylor_term (expr,ord):
    return ((x**ord)*(diff(expr,x,ord).subs(x,0)))/factorial(ord) 

for i in range(order):
    if(taylor_term(y,i)):
        print(taylor_term(y,i))