# A Python complex number z is stored internally using rectangular or Cartesian
# coordinates. It is completely determined by its real part z.real and its
# imaginary part z.imag.

# Polar coordinates give an alternative way to represent a complex number.
# In polar coordinates, a complex number z is defined by the modulus r and
# the phase angle phi. The modulus r is the distance from z to the origin,
# while the phase phi is the counterclockwise angle, measured in radians, from
# the positive x-axis to the line segment that joins the origin to z.

# cmath.phase(x) - return the phase of x. phase(x) is equivalent to
# math.atan2(x.imag, x.real)

# cmath.polar(x) - return the representation of x in polar coordinates. Returns
# a pair (r, phi) where r is the modulus of x and phi is the phase of x.
# equivalent to (abs(x), phase(x))

# cmath.rect(r, phi) - return the complex number x with polar coordinates r 
# and phi.
# Equivalent to r * (math.cos(phi)) + math.sin(phi)*1j)

# ! complex() function can be used in python to convert the input as complex
# number.

# Polar coordinates are an alternative way of representing Cartesian
# coordinates or complex numbers.

# Input format:
# a single line comtaining the complex number z.

# Output format:
# two lines: 1) contain the value of r
#            2) contain the value of phi

import cmath

z = complex(input())

r, phi = cmath.polar(z)

print(f'Polar coordinates of z = {z}\nr = {r}\nphi = {phi}')
