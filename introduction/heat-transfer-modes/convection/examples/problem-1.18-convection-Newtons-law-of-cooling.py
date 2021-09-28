# -*- coding: utf-8 -*-
"""
Heat Transfer I                                                 July 21, 2020
ME 3150 FA20  
Prof. M. Diaz-Maldonado

Synopsis:
Problem 1.18. Newton's law of cooling. Cooling surface. Conceptual Problem.
Calculate the heat rate from the surface to the moving fluid.

Incroprera et al. Fundamentals of Heat and Mass Transfer, 8th edition. 
Physical quantities are expressed in SI Units.
"""


"""
Part a. Air
heat transfer coefficient,        W / m^2 K
surface temperature,      Kelvin, K
ambient temperature,      Kelvin, K
"""
h     = 40.0
T_s   = 30.0 + 273.15
T_inf = -5.0 + 273.15
""" 
Solution:
heat flux, Watts per meter squared, W/m^2
"""
q = h * (T_s - T_inf)

print("")
print("Answers:")
print("part a.")
print("heat flux: %6.2f W/m^2" %(q) )
print("")

"""
Part a. Water
heat transfer coefficient,        W / m^2 K
surface temperature,      Kelvin, K
ambient temperature,      Kelvin, K
"""
h     = 900.0
T_s   = 30.0 + 273.15
T_inf = 10.0 + 273.15
""" 
Solution:
heat flux, Watts per meter squared, W/m^2
"""
q = h * (T_s - T_inf)

print("part b.")
print("heat flux: %6.2f W/m^2" %(q) )
print("")