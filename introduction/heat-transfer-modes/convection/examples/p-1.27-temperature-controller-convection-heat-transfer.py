#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Heat Transfer I                                              March 23, 2020
ME 3150 SP20
Prof. M. Diaz-Maldonado

Synopsis:
Problem 1.27.
Heat removal from a temperature controller by forced convection.


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

ans = (
    f"\n\nProblem 1.27: Temperature Controller\n"
    f"max power: {Eg:12.4e} W\n\n"
)
print(ans)
