from typing import List
from city import City

class Route:
    """
    La clase `Route` representa una posible solución al problema presentado.
    Este representa la parte del cromosoma en el *framework* de los algoritmos genéticos.
    """

    def __init__(self, cities: List[City], mutation_probability: int, cut_point: int):
        self.cities = cities
        self.mutation_probability = mutation_probability
        self.cut_point = cut_point
        self.distance = sum((a.distance(b) for a, b in zip(cities[:-1], cities[1:])))
