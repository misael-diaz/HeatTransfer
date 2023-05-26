#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Heat Transfer I                                               July 21, 2020
ME 3150 FA20
Prof. M. Diaz-Maldonado

Synopsis:
Problem 1.28. Heat removal from a steam pipe by convection.
Physical quantities are expressed in SI Units.


Copyright (c) 2021 Misael Diaz-Maldonado
This file is released under the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.


References:
[0] R Johansson, Numerical Python: Scientific Computing and Data
    Science Applications with NumPy, SciPy, and Matplotlib, 2nd edition.
[1] TL Bergman, AS Lavine, FP Incropera, DP DeWitt, Fundamentals of Heat
    and Mass Transfer, 8th edition.
"""

from numpy import pi

"""
Given:
"""
L = 25                      # length,       m
D = 0.1                     # diameter,     m
A = pi * D * L              # surface area, m^2

h     = 45                  # heat transfer coefficient,    W / (m^2 K)
T_s   = 150 + 273.15        # surface temperature,          K
T_inf = 25  + 273.15        # ambient temperature,          K

""" 
Solution:
"""
q = h * A * (T_s - T_inf)   # rate of heat transfer,    W

ans = (
    f"\n\nProblem 1.28: "
    f"Heat Transfer from a Steam Pipe by Forced Convection\n"
    f"rate of heat loss: {(1e-3 * q):6.2f} kW\n\n"
)
print(ans)
