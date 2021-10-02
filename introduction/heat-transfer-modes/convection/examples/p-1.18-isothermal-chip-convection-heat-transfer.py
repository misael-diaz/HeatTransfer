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

from numpy import array

"""
Given:
"""
L = 5.0e-3  # squared chip length,  m
T_s   = 85  # surface temperature,  C
T_inf = 15  # ambient temperature,  C

""" heat transfer coeffs of air and dielectric fluid, respectively """
h = array([200, 3000]) # W / m^2 K

"""
Knowledge:
"""
A = L * L   # chip's surface area,  m^2

"""
Solution (parts a and b):
"""
Eg = part_a, part_b = h * A * (T_s - T_inf) # dissipated thermal energy, W

ans = (
    f"\n\nProblem 1.18 (6th ed): "
    f"Chip Cooling by Forced Convection\n"
    f"max power for air-cooled chip:              {part_a:6.2f} W\n"
    f"max power for dielectric fluid-cooled chip: {part_b:6.2f} W\n\n"
)
print(ans)
