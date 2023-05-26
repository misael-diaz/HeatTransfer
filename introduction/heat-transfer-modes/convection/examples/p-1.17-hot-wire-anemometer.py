#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Heat Transfer I                                              March 16, 2020
ME 3150 SP20
Prof. M. Diaz-Maldonado

Synopsis:
Problem 1.17 (6th ed). Hot-wire Anemometer, an air speed measuring device.
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
Given:
"""
L = 20.0e-3     # wire length,              meters,         m
D =  0.5e-3     # wire diameter,            meters,         m
e_R = 5.0       # resistance voltage drop,  Volts,          V
I   = 0.1       # electric current,         Amperes,        A
T_s   = 75      # wire surface temperature, Centigrades,    C
T_inf = 25      # ambient temperature,      Centigrades,    C

"""
Knowledge:
"""
A = pi * D * L  # wire surface area,        meters squared, m^2
Eg = e_R * I    # generated thermal energy, Watts,          W

"""
Solution:
"""
h = Eg / ( A * (T_s - T_inf) )  # convection coefficient,   W / (m^2 K)
U = 6.25e-5 * h**2              # air speed,                m / s

ans = (
    f"\n\nProblem 1.17 (6th-edition):\n"
    f"Hot-wire anemometer (an air speed measuring apparatus)\n"
    f"convection heat transfer coefficient: {h:8.2f} W/(m^2 K)\n"
    f"air speed:                            {U:8.2f} m/s\n\n"
)

print(ans)
