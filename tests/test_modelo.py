import sys, os, math
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from campana import CampanaPruebas

defectos = [28, 23, 22, 17, 16, 12, 12, 9]

datos = []
for i in range(len(defectos)):
    datos.append({"semana": i + 1, "defectos": defectos[i]})


def test_goel_cero():
    camp = CampanaPruebas(datos)
    a, b = camp.ajustar()
    assert camp.goel(0, 100, 0.2) == 0
    assert camp.goel(0, a, b) == 0


def test_acumulados():
    camp = CampanaPruebas(datos)
    assert camp.acumulados[-1] == 139


def test_restantes():
    camp = CampanaPruebas(datos)
    res = camp.restantes()
    assert res["a"] >= 139
    assert res["restantes"] > 0
    assert abs(res["semana_95"] - math.log(20) / res["b"]) < 0.001


if __name__ == "__main__":
    test_goel_cero()
    test_acumulados()
    test_restantes()
    print("todo bien")