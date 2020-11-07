from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class City:  # This is a gene
    """
    La clase `City` representa uno de los parámetros que forman parte de la solución a nuestro problema.
    Este representa la parte del gen en el *framework* de los algoritmos genéticos.
    """

    name: str
    x: int
    y: int

    def distance(self, city: City) -> float:
        xx = city.x - self.x
        yy = city.y - self.y
        return math.sqrt(xx ** 2 + yy ** 2)
