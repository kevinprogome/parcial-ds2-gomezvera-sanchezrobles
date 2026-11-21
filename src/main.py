
from pymongo import MongoClient
from campana import CampanaPruebas


cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["huilasoft"]

defectos = list(db.defectos_semana.find({}, {"_id": 0}))

campana = CampanaPruebas(defectos)

a, b = campana.ajustar()

print("MODELO DE GOEL-OKUMOTO")
print("Total estimado de defectos:", round(a, 2))
print("Ritmo de detección:", round(b, 5))

resultado = campana.restantes()

print("RESULTADOS DE LA CAMPAÑA")
print("Defectos encontrados:", round(resultado["encontrados"], 2))
print("Defectos restantes:", round(resultado["restantes"], 2))
print("Semana para alcanzar el 95%:", round(resultado["semana_95"], 2))

assert campana.goel(0, 100, 0.2) == 0
assert abs(campana.goel(1, 100, 0.2) - 18.1269) < 0.001

print("Las dos pruebas fueron exitosas.")

campana.graficar()

cliente.close()
