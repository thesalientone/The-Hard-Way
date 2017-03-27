from sympy import *

x, t, z, nu = symbols('x t z nu')
print solve(x ** 2 - 5 )

y = Function('y')
h = dsolve(Eq(y(t).diff(t,t) - y(t), exp(t)), y(t))
print y
print h


expr = cos(x) + 1


print expr.subs(x,2).evalf()

print cos(5).evalf()
print cos(7).evalf()
