import sys
import os
import math

raiz = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, raiz)
sys.path.insert(0, os.path.join(raiz, "src"))

from campana import CampanaPruebas


defectos = [28, 23, 22, 17, 16, 12, 12, 9]
datos = [{"semana": i + 1, "defectos": d} for i, d in enumerate(defectos)]


def test_goel_en_cero():
    campana = CampanaPruebas(datos)
    a, b = campana.ajustar()

    assert campana.goel(0, 100, 0.2) == 0
    assert campana.goel(0, a, b) == 0


def test_acumulados_y_ajuste():
    campana = CampanaPruebas(datos)
    resultado = campana.restantes()

    assert campana.acumulados[-1] == 139
    assert resultado["a"] >= 139
    assert resultado["restantes"] > 0
    assert abs(resultado["semana_95"] - math.log(20) / resultado["b"]) < 0.0001


if __name__ == "__main__":
    test_goel_en_cero()
    test_acumulados_y_ajuste()
    print("Las dos pruebas pasaron.")