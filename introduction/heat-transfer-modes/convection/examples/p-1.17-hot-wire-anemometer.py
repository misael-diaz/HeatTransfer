#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Heat Transfer I                                                 March 16, 2020
ME 3150 SP20
Prof. M. Diaz-Maldonado

Synopsis:
Problem 1.17. Hot-wire Anemometer, a device which measures the air speed.
Incroprera et al. Fundamentals of Heat and Mass Transfer, 6th edition.
Physical quantities are expressed in SI Units.
"""

from numpy import pi

"""
length,   meters,         m
diameter, meters,         m
area,     meters squared, m^2
"""
L = 20.0e-3
D =  0.5e-3
A = pi * D * L # exposed surface area of wire (cylinder)

"""
resistance voltage drop,  Volts,    V
electric current,         Amperes,  A
generated thermal energy, Watts,    W
"""
e_R = 5.0
I   = 0.1
Eg = e_R * I

"""
wire surface temperature, Centigrades, C
ambient temperature,      Centigrades, C
"""
T_s   = 75.0
T_inf = 25.0

"""
convection heat transfer coefficient, W/(m^2 K)
air speed,                            m/s
"""
h = Eg / ( A * (T_s - T_inf) )
U = 6.25e-5 * h**2

print("")
print("Answers:")
print("convection heat transfer coefficient: %e W/(m^2 K)" %(h))
print("air speed:                            %e m/s" %(U))
print("")
