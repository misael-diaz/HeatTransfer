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
length,                     meters,         m
total surface area (cube),  meters squared, m^2
"""
W = 0.3
A = 6 * W * W

"""
power input,                horsepower,     hp
transmission efficiency,    dimensionless,  1
generated thermal energy,   Watts,          W
"""
P   = 150.0
eta = 0.93
Eg  = P * (1 - eta) * 0.7457e3; # constant converts hp to W

"""
heat transfer coefficient,                  W / (m^2 K)
ambient temperature,        Centigrades,    C
"""
h     = 200.0
T_inf = 30.0

"""
solution:
transmission temperature, Centigrades, C
"""
T_s = Eg / (h * A) + T_inf

ans = (
    f"\n\nProblem 1.23 (6th edition): Forced Convection\n"
    f"Solution:\n"
    f"surface temperature of transmission: {T_s:6.2f} centigrades\n\n"
)
print(ans)
