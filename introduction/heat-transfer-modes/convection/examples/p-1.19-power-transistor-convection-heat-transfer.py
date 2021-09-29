#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Heat Transfer I                                              March 23, 2020
ME 3150 SP20  
Prof. M. Diaz-Maldonado

Synopsis:
Problem 1.27. Heat removal from a power transistor by forced convection.

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
L = 10.0e-3
D = 12.0e-3
A = pi * D * L

"""
heat transfer coefficient,             W / m^2 K
surface temperature,      Centigrades, C
ambient temperature,      Centigrades, C
"""
h     = 100.0
T_s   = 85.0
T_inf = 25.0

""" 
solution (part a):
generated thermal energy, Watts,         W
"""
Eg = h * A * (T_s - T_inf)

print("")
print("Answers:")
print("max allowed power: %e W" %(Eg))
print("")
