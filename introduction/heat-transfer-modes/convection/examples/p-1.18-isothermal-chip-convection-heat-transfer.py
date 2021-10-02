#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Heat Transfer I                                                 March 23, 2020
ME 3150 SP20
Prof. M. Diaz-Maldonado

Synopsis:
Problem 1.18 (1.26 8th edition).
Heat removal from an isothermal chip by forced convection.
Physical quantities are expressed in SI Units.


Copyright (c) 2021 Misael Diaz-Maldonado
This file is released under the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.


References:
[0] R Johansson, Numerical Python: Scientific Computing and Data
    Science Applications with NumPy, SciPy, and Matplotlib, 2nd edition
[1] TL Bergman, AS Lavine, FP Incropera, DP DeWitt, Fundamentals of Heat
    and Mass Transfer, 8th edition.
"""

"""
length,         meters,         m
surface area,   meters squared, m^2
"""
W = 5.0e-3
A = W * W

"""
heat transfer coefficient,                  W / m^2 K
surface temperature,        Centigrades,    C
ambient temperature,        Centigrades,    C
"""
h     = 200.0
T_s   = 85.0
T_inf = 15.0

"""
solution (part a):
generated thermal energy,   Watts,  W
"""
Eg = h * A * (T_s - T_inf)

print("")
print("Answers:")
print("max allowed chip power with air as coolant: %e W" %(Eg))
"""
convection heat transfer coefficient for the dielectric fluid, W / m^2 K
"""
h = 3000.0
"""
solution (part b):
generated thermal energy,   Watts,  W
"""
Eg = h * A * (T_s - T_inf)
print("max allowed chip power with the dielectric fluid as coolant: %e W" %(Eg))
print("")
