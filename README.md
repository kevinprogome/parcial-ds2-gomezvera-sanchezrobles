HuilaSoft
Kevin Raul Gomez Vera
Jeisson Esteban Sanchez Robles

Parte 1: 
Se crearon 3 colecciones: agentes,ticket y defectos_semana

La coleccion de agentes tienen: nombre, nivel tickethora y si es un agente activo

La coleccion de ticket tiene: codigo, llegada_min, atencion_min, prioridad, agente

La coleccion defectos_semana tiene: semana, defectos, version

Parte 2:

Opcion seleccionada B - Evolución del Sofware

se creo la clase campanapruebas que recive los datos de coleccion de defectos_semana de mongobd y acumula los defectos encontrados durante 8 semanas

el programa se ejecuta desde main.py donde se conecta con mongodb consulta los datos, crea un objeto y mnuestra los resultados


librerias utilizadas
pymongo
numpy
scipy
matplotlib


campana.py es un archivo adaptado al tema 5 "Evolucion de sistemas" 

INTERPRETACION:
El modelo describe bien los datos, esto debido a que la curva naranja pasa por todos los puntos azules, Teniendo un R2 aproximado a 0.9998, por lo que podemos concluir que las estimaciones del modelo son confiables, al principio aparecen 28 defectos en la 1 semana y en la semana 8 solamente 9, el ritmo actual es de unos 9 defectos por semana
Si se estuviera cerca por terminar la linea se veria horizontal al final, pero podemos observar que todavia sube, esto significa que siguen apareciendo defectos, segun el modelo se alcanzaria hasta la semana 19-20 unas 12 semanas mas.
