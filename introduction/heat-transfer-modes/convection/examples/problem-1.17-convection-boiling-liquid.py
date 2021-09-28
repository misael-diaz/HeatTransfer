# -*- coding: utf-8 -*-
"""
Heat Transfer I                                                 July 21, 2020
ME 3150 FA20  
Prof. M. Diaz-Maldonado

Synopsis:
Problem 1.17. Convection from a hot plate to the surface of a boiling liquid.

Incroprera et al. Fundamentals of Heat and Mass Transfer, 8th edition. 
Physical quantities are expressed in SI Units.
"""


"""
Part a. Water
heat transfer coefficient,        W / m^2 K
ambient temperature,      Kelvin, K
heat flux, Watts per meter squared,         W/m^2
"""
h     = 20.0e3
T_inf = 100.0  + 273.15
q     = 20.0e5
""" 
Solution:
hot plate temperature,      Kelvin, K
"""
T_s = q/h + T_inf

print("")
print("Answers:")
print("part a.")
print("temperature of hot plate: %6.2f C" %(T_s - 273.15) )
print("")

"""
Part b. Dielectric liquid
heat transfer coefficient,        W / m^2 K
ambient temperature,      Kelvin, K
heat flux, Watts per meter squared,         W/m^2
"""
h     = 3.0e3
T_inf = 52.0 + 273.15
q     = 20.0e5
""" 
Solution:
hot plate temperature,      Kelvin, K
"""
T_s = q/h + T_inf

print("part b.")
print("temperature of hot plate: %6.2f K" %(T_s) )
