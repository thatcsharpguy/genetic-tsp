from __future__ import annotations
import math

class City: # This is a gene
    """
    La clase `City` representa uno de los parámetros que forman parte de la solución a nuestro problema.
    Este representa la parte del gen en el *framework* de los algoritmos genéticos.
    """

    def __init__(self, x: int, y: int, name: str):
        self.x = x
        self.y = y
        self.name = name
    
    def distance(self, city: City):
        xx = city.x - self.x
        yy = city.y - self.y
        return math.sqrt(xx ** 2 + yy ** 2)
