# -*- coding: utf-8 -*-
"""
Heat Transfer I                                                 March 23, 2020
ME 3150 SP20  
Prof. M. Diaz-Maldonado

Synopsis:
Problem 1.23. Heat removal from a transmission case by forced convection.

Incroprera et al. Fundamentals of Heat and Mass Transfer, 7th edition. 
Physical quantities are expressed in SI Units.
"""

"""
length,   meters,         m
total surface area (cube),     meters squared, m^2
"""
W = 0.3
A = 6 * W * W

"""
power input,              horsepower,    hp
transmission efficiency,  dimensionless, 1
generated thermal energy, Watts,         W
"""
P   = 150.0
eta = 0.93
Eg  = P * (1 - eta) * 0.7457e3; # constant converts hp to W  

"""
heat transfer coefficient,             W / m^2 K
ambient temperature,      Centigrades, C
"""
h     = 200.0
T_inf = 30.0

""" 
solution:
transmission temperature, Centigrades, C
"""
T_s = Eg / (h * A) + T_inf 

print("")
print("Answers:")
print("surface temperature of transmission: %6.2f centigrades" %(T_s))
print("")
