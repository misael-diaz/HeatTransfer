#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Heat Transfer I                                               July 21, 2020
ME 3150 FA20
Prof. M. Diaz-Maldonado

Synopsis:
Problem 1.28. Heat removal from a steam pipe by convection.

Incroprera et al. Fundamentals of Heat and Mass Transfer, 7th edition.
Physical quantities are expressed in SI Units.
"""

import math
pi = math.pi

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
    f"rate of heat loss: %{(1e-3 * q):6.2f} kW\n\n"
)
print(ans)
