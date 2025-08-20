"""
A01647993 Christian André Salgado Ledezma
A01648054 Damaris Mariel Ramos Mariscal
A016
A016
A016
"""

import math
import tkinter as tk

root = tk.Tk()
root.geometry("800x600")

label = tk.Label(root, text="Exoplanet Information Calculator", font=("Arial", 24))
label.pack(padx=20, pady=20)

label = tk.Label(root, text="Select the equation you want to solve:", font=("Arial", 18))
label.pack(pady=10)

btn_pad = 16

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.45, anchor='center')

frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

button_font = ("Arial", 14)
btn_pad = 10
btn_ipady = 15

buttonExcentricity = tk.Button(frame, text="Excentricity", font=button_font, width=15)
buttonExcentricity.grid(row=0, column=0, padx=btn_pad, pady=btn_pad, ipady=btn_ipady, sticky='ew')

buttonOrbitalPeriod = tk.Button(frame, text="Orbital Period", font=button_font, width=15)
buttonOrbitalPeriod.grid(row=0, column=1, padx=btn_pad, pady=btn_pad, ipady=btn_ipady, sticky='ew')

buttonMajorAxis = tk.Button(frame, text="Major Axis", font=button_font)
buttonMajorAxis.grid(row=1, column=0, padx=btn_pad, pady=btn_pad, ipady=btn_ipady, sticky='ew')

buttonMinorAxis = tk.Button(frame, text="Minor Axis", font=button_font)
buttonMinorAxis.grid(row=1, column=1, padx=btn_pad, pady=btn_pad, ipady=btn_ipady, sticky='ew')

buttonPerihelion = tk.Button(frame, text="Perihelion", font=button_font)
buttonPerihelion.grid(row=2, column=0, padx=btn_pad, pady=btn_pad, ipady=btn_ipady, sticky='ew')

buttonAphelion = tk.Button(frame, text="Aphelion", font=button_font)
buttonAphelion.grid(row=2, column=1, padx=btn_pad, pady=btn_pad, ipady=btn_ipady, sticky='ew')

root.mainloop()

G = 6.67428e-11  # Gravitational constant in m^3 kg^-1 s^-2
M = float(input("Enter the mass of the central body in kilograms: "))

excentricity = float(input("Enter the eccentricity of the orbit: "))
orbitalPeriod = float(input("Enter the orbital period in seconds: "))
majorAxis = float(input("Enter the semi-major axis in meters: "))
minorAxis = float(input("Enter the semi-minor axis in meters: "))
perihelion = float(input("Enter the perihelion distance in meters: "))
aphelion = float(input("Enter the aphelion distance in meters: "))

def excentricityCalculator(majorAxis, minorAxis):
    """
    Calculate the excentricity of an ellipse given its semi-major axis (a) and semi-minor axis (b).
    
    Parameters:
    a (float): Semi-major axis of the ellipse.
    b (float): Semi-minor axis of the ellipse.
    
    Returns:
    float: Excentricity of the ellipse.
    """
    if majorAxis <= 0 or minorAxis <= 0:
        raise ValueError("Semi-major and semi-minor axes must be positive numbers.")
    
    return math.sqrt(1 - (minorAxis**2 / majorAxis**2))

def orbitalPeriodCalculator(majorAxis, M):
    """
    Calculate the orbital period of a planet using Kepler's third law.
    
    Parameters:
    a (float): Semi-major axis of the orbit in meters.
    M (float): Mass of the central body in kilograms.
    
    Returns:
    float: Orbital period in seconds.
    """
    if majorAxis <= 0 or M <= 0:
        raise ValueError("Semi-major axis and mass must be positive numbers.")
    
    return 2 * math.pi * math.sqrt(majorAxis**3 / (G * M))

def majorAxisCalculator(perihelion, aphelion):
    """
    Calculate the semi-major axis of an orbit given the perihelion and aphelion distances.
    
    Parameters:
    perihelion (float): Distance at the closest approach to the central body in meters.
    aphelion (float): Distance at the farthest point from the central body in meters.
    
    Returns:
    float: Semi-major axis in meters.
    """
    if perihelion <= 0 or aphelion <= 0:
        raise ValueError("Perihelion and aphelion must be positive numbers.")
    
    return (perihelion + aphelion) / 2

def minorAxisCalculator(majorAxis, excentricity):
    """
    Calculate the semi-minor axis of an orbit given the semi-major axis and excentricity.
    
    Parameters:
    majorAxis (float): Semi-major axis of the orbit in meters.
    excentricity (float): Excentricity of the orbit.
    
    Returns:
    float: Semi-minor axis in meters.
    """
    if majorAxis <= 0 or not (0 <= excentricity < 1):
        raise ValueError("Semi-major axis must be positive and excentricity must be in the range [0, 1).")
    
    return majorAxis * math.sqrt(1 - excentricity**2)

def perihelionCalculator(majorAxis, excentricity):
    majorAxis * (1 - excentricity)

def aphelionCalculator(majorAxis, excentricity):
    majorAxis * (1 + excentricity)