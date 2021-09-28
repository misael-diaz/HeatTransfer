# -*- coding: utf-8 -*-
"""
Heat Transfer I                                                 March 23, 2020
ME 3150 SP20  
Prof. M. Diaz-Maldonado

Synopsis:
Problem 1.27. Heat removal from a temperature controller by forced convection.

Incroprera et al. Fundamentals of Heat and Mass Transfer, 7th edition. 
Physical quantities are expressed in SI Units.
"""

"""
surface area,     meters squared, m^2
"""
A = 30.0e-6

"""
heat transfer coefficient,             W / m^2 K
surface temperature,      Centigrades, C
ambient temperature,      Centigrades, C
"""
h     = 25.0
T_s   = 70.0
T_inf = 50.0

""" 
solution (part a):
generated thermal energy, Watts,         W
"""
Eg = h * A * (T_s - T_inf) 

print("")
print("Answers:")
print("max power: %e W" %(Eg))
print("")
