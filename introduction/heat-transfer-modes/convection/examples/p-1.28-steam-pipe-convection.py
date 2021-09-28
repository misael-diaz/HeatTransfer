# -*- coding: utf-8 -*-
"""
Heat Transfer I                                                 July 21, 2020
ME 3150 FA20  
Prof. M. Diaz-Maldonado

Synopsis:
Problem 1.28. Heat removal from a steam pipe by convection.

Incroprera et al. Fundamentals of Heat and Mass Transfer, 7th edition. 
Physical quantities are expressed in SI Units.
"""

import math
pi = math.pi

"""
length,           meters,         m
diameter,         meters,         m
surface area,     meters squared, m^2
"""
L = 25.0
D = 0.1
A = pi * D * L 

"""
heat transfer coefficient,        W / m^2 K
surface temperature,      Kelvin, K
ambient temperature,      Kelvin, K
"""
h     = 45.0
T_s   = 150.0 + 273.15
T_inf = 25.0  + 273.15
""" 
Solution:
rate of heat transfer, Watts,         W
"""
q = h * A * (T_s - T_inf)

print("")
print("Answers:")
print("rate of heat loss: %6.2f kW" %(1e-3 * q))
print("")
