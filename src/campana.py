
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import math


class CampanaPruebas:

    def __init__(self, defectos):
        defectos = sorted(defectos, key=lambda x: x["semana"])

        self.t = np.array([d["semana"] for d in defectos], dtype=float)
        nuevos = np.array([d["defectos"] for d in defectos], dtype=float)

        self.acumulados = np.cumsum(nuevos)
        self.a = None
        self.b = None

    def goel(self, t, a, b):
        return a * (1 - np.exp(-b * t))

    def ajustar(self):
        semilla = [max(self.acumulados) * 1.3, 0.2]

        limites = ([max(self.acumulados), 0.001],
                   [max(self.acumulados) * 50, 5.0])

        parametros, _ = curve_fit(
            self.goel,
            self.t,
            self.acumulados,
            p0=semilla,
            bounds=limites,
            maxfev=50000
        )

        self.a, self.b = parametros

        return self.a, self.b

    def restantes(self):
        if self.a is None:
            self.ajustar()

        encontrados = self.goel(self.t[-1], self.a, self.b)
        faltantes = self.a - encontrados
        semana_95 = math.log(20) / self.b

        return {
            "a": self.a,
            "b": self.b,
            "encontrados": encontrados,
            "restantes": faltantes,
            "semana_95": semana_95
        }

    def graficar(self):
        if self.a is None:
            self.ajustar()

        figura, eje = plt.subplots(figsize=(9, 4))

        eje.plot(self.t, self.acumulados, marker="o",
                 label="Datos reales")

        tiempo = np.linspace(0, self.t[-1], 100)

        eje.plot(tiempo, self.goel(tiempo, self.a, self.b),
                 linewidth=2, label="Modelo Goel-Okumoto")

        eje.set_xlabel("Semanas de prueba")
        eje.set_ylabel("Defectos acumulados")
        eje.set_title("Evolución de los defectos de Huilasoft")
        eje.legend()
        eje.grid(True)

        plt.tight_layout()
        plt.show()
