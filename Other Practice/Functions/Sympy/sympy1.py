from sympy import *

x = symbols('x')

a = Integral(cos(x)*exp(x),x)

b = a.doit()

print Eq(a, a.doit())
print b
