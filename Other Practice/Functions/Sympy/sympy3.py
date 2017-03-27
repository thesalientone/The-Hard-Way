from sympy import *
import random
import cmath

x = symbols('x')

level = 3
coefficients = [int(11 * random.random()) for i in xrange(0,level)]
powers = [int(11 * random.random()) for i in xrange(0,level)]

polynomials = []
print coefficients
print powers
for i in xrange(0,level):
    polynomials.append(coefficients[i])
    polynomials.append("* x ** ")
    polynomials.append(powers[i])
    if i < level - 1:
        polynomials.append("+")

print polynomials

nomial = ' '.join(map(str, polynomials))
print nomial
