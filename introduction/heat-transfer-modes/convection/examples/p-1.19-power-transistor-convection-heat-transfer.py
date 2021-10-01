#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Heat Transfer I                                              March 23, 2020
ME 3150 SP20  
Prof. M. Diaz-Maldonado

Synopsis:
Problem 1.27 (8th edition).
Heat removal from a power transistor by forced convection.
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

from numpy import pi

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

ans = (
    f"\n\nProblem 1.27 (1.19 6th-ed):\n"
    f"Heat transfer from a power transistor by forced convection\n\n"
    f"Solution:\n"
    f"max allowed power: {Eg} W\n\n"
)
print(ans)
