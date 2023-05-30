#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Heat Transfer I                                              March 23, 2020
ME 3150 SP20
Prof. M. Diaz-Maldonado

Synopsis:
Problem 1.23 (6th edition).
Heat removal from a transmission case by forced convection.
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
Given:
"""
L = 0.3                     # length,                   m
P = 150                     # power input,              hp
eta = 0.93                  # transmission efficiency,  1
h = 200                     # convection coefficient,   W / (m^2 K)
T_inf = 30                  # ambient temperature,      C

"""
Knowledge:
"""
A   = 6 * L * L             # surface area (cube),      m^2
Eg  = P * (1 - eta)         # dissipated energy,        hp
Eg *= 0.7457e3              # hp -> W

"""
Solution:
"""
T_s = Eg / (h * A) + T_inf  # transmission temperature, C

ans = (
    f"\n\nProblem 1.23 (6th edition): Forced Convection\n"
    f"Solution:\n"
    f"surface temperature of transmission: {T_s:6.2f} centigrades\n\n"
)
print(ans)
