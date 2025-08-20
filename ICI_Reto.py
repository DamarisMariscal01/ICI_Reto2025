import math
import tkinter as tk
from tkinter import messagebox

# Constante gravitacional
G = 6.67428e-11  

class ExoplanetApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Exoplanet Information Calculator")

        # Mostrar la página inicial
        self.home_page()

    def clear_frame(self):
        """Eliminar todos los widgets de la ventana"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def home_page(self):
        """Mostrar la página principal con 6 botones"""
        self.clear_frame()

        tk.Label(self.root, text="Exoplanet Information Calculator", font=("Arial", 24)).pack(pady=20)
        tk.Label(self.root, text="Select the equation you want to solve:", font=("Arial", 18)).pack(pady=10)

        frame = tk.Frame(self.root)
        frame.place(relx=0.5, rely=0.45, anchor="center")

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        button_font = ("Arial", 14)
        btn_pad = 10
        btn_ipady = 15

        # Botones de operaciones
        buttons = [
            ("Excentricity", self.excentricity_page),
            ("Orbital Period", self.orbital_period_page),
            ("Major Axis", self.major_axis_page),
            ("Minor Axis", self.minor_axis_page),
            ("Perihelion", self.perihelion_page),
            ("Aphelion", self.aphelion_page)
        ]

        # Crear botones en grid 2x3
        for i, (text, command) in enumerate(buttons):
            row, col = divmod(i, 2)
            tk.Button(frame, text=text, font=button_font, width=15, command=command)\
                .grid(row=row, column=col, padx=btn_pad, pady=btn_pad, ipady=btn_ipady, sticky="ew")

    def show_result(self, result):
        """Mostrar el resultado y botón Done"""
        self.clear_frame()
        tk.Label(self.root, text=f"Result: {result}", font=("Arial", 18)).pack(pady=30)
        tk.Button(self.root, text="Done", width=20, height=2, command=self.home_page).pack(pady=20)

    # ---- PÁGINAS PARA CADA CÁLCULO ----

    def excentricity_page(self):
        """Calcular excentricidad"""
        self.clear_frame()
        tk.Label(self.root, text="Excentricity Calculator", font=("Arial", 18)).pack(pady=20)

        tk.Label(self.root, text="Semi-major axis (a) [m]:").pack()
        entry_a = tk.Entry(self.root)
        entry_a.pack(pady=5)

        tk.Label(self.root, text="Semi-minor axis (b) [m]:").pack()
        entry_b = tk.Entry(self.root)
        entry_b.pack(pady=5)

        def calculate():
            try:
                a = float(entry_a.get())
                b = float(entry_b.get())
                result = math.sqrt(1 - (b**2 / a**2))
                self.show_result(result)
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.root, text="Calculate", command=calculate).pack(pady=20)

    def orbital_period_page(self):
        """Calcular periodo orbital"""
        self.clear_frame()
        tk.Label(self.root, text="Orbital Period Calculator", font=("Arial", 18)).pack(pady=20)

        tk.Label(self.root, text="Semi-major axis (a) [m]:").pack()
        entry_a = tk.Entry(self.root)
        entry_a.pack(pady=5)

        tk.Label(self.root, text="Mass of central body (M) [kg]:").pack()
        entry_m = tk.Entry(self.root)
        entry_m.pack(pady=5)

        def calculate():
            try:
                a = float(entry_a.get())
                M = float(entry_m.get())
                result = 2 * math.pi * math.sqrt(a**3 / (G * M))
                self.show_result(result)
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.root, text="Calculate", command=calculate).pack(pady=20)

    def major_axis_page(self):
        """Calcular semi-eje mayor"""
        self.clear_frame()
        tk.Label(self.root, text="Major Axis Calculator", font=("Arial", 18)).pack(pady=20)

        tk.Label(self.root, text="Perihelion (q) [m]:").pack()
        entry_q = tk.Entry(self.root)
        entry_q.pack(pady=5)

        tk.Label(self.root, text="Aphelion (Q) [m]:").pack()
        entry_Q = tk.Entry(self.root)
        entry_Q.pack(pady=5)

        def calculate():
            try:
                q = float(entry_q.get())
                Q = float(entry_Q.get())
                result = (q + Q) / 2
                self.show_result(result)
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.root, text="Calculate", command=calculate).pack(pady=20)

    def minor_axis_page(self):
        """Calcular semi-eje menor"""
        self.clear_frame()
        tk.Label(self.root, text="Minor Axis Calculator", font=("Arial", 18)).pack(pady=20)

        tk.Label(self.root, text="Semi-major axis (a) [m]:").pack()
        entry_a = tk.Entry(self.root)
        entry_a.pack(pady=5)

        tk.Label(self.root, text="Excentricity (e):").pack()
        entry_e = tk.Entry(self.root)
        entry_e.pack(pady=5)

        def calculate():
            try:
                a = float(entry_a.get())
                e = float(entry_e.get())
                result = a * math.sqrt(1 - e**2)
                self.show_result(result)
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.root, text="Calculate", command=calculate).pack(pady=20)

    def perihelion_page(self):
        """Calcular perihelio"""
        self.clear_frame()
        tk.Label(self.root, text="Perihelion Calculator", font=("Arial", 18)).pack(pady=20)

        tk.Label(self.root, text="Semi-major axis (a) [m]:").pack()
        entry_a = tk.Entry(self.root)
        entry_a.pack(pady=5)

        tk.Label(self.root, text="Excentricity (e):").pack()
        entry_e = tk.Entry(self.root)
        entry_e.pack(pady=5)

        def calculate():
            try:
                a = float(entry_a.get())
                e = float(entry_e.get())
                result = a * (1 - e)
                self.show_result(result)
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.root, text="Calculate", command=calculate).pack(pady=20)

    def aphelion_page(self):
        """Calcular afelio"""
        self.clear_frame()
        tk.Label(self.root, text="Aphelion Calculator", font=("Arial", 18)).pack(pady=20)

        tk.Label(self.root, text="Semi-major axis (a) [m]:").pack()
        entry_a = tk.Entry(self.root)
        entry_a.pack(pady=5)

        tk.Label(self.root, text="Excentricity (e):").pack()
        entry_e = tk.Entry(self.root)
        entry_e.pack(pady=5)

        def calculate():
            try:
                a = float(entry_a.get())
                e = float(entry_e.get())
                result = a * (1 + e)
                self.show_result(result)
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.root, text="Calculate", command=calculate).pack(pady=20)


# ---- EJECUTAR APP ----
if __name__ == "__main__":
    root = tk.Tk()
    app = ExoplanetApp(root)
    root.mainloop()