#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Heat Transfer I                                              March 23, 2020
ME 3150 SP20  
Prof. M. Diaz-Maldonado

Synopsis:
Problem 1.27.
Heat removal from a temperature controller by forced convection.

Incroprera et al. Fundamentals of Heat and Mass Transfer, 7th edition. 
Physical quantities are expressed in SI Units.
"""

"""
Given:
"""
A = 30.0e-6     # surface area, m^2

h     = 25.0    # heat transfer coefficient, W / (m^2 * K)
T_s   = 70.0    # surface temperature, C
T_inf = 50.0    # ambient temperature, C

"""
Solution:
"""
Eg = h * A * (T_s - T_inf)  # dissipated thermal energy, W

print("")
print("Answers:")
print("max power: %e W" %(Eg))
print("")
