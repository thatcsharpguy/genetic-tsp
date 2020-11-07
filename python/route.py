from collections import UserList
from typing import Sequence

from city import City


class Route(UserList):
    """
    La clase `Route` representa una posible solución al problema presentado.
    Este representa la parte del cromosoma en el *framework* de los algoritmos genéticos.
    """

    def __init__(self, cities: Sequence[City]):
        self.data = cities
        self.distance = sum(
            (a.distance(b) for a, b in zip(self.data[:-1], self.data[1:]))
        )

    def __str__(self):
        def extract_city_info(city: City):
            return str(city)

        representation = ""
        # if len(self) > 6:
        #    left = [extract_city_info(city) for city in self.data[:3]]
        #    right = [extract_city_info(city) for city in self.data[-3:]]
        #    cities = ", ".join(left) + ", ..., " + ", ".join(right)
        # else:
        cities = ", ".join([extract_city_info(city) for city in self.data])

        return f"{self.distance:0.3f} [{cities}]"

    def __repr__(self):
        return str(self)
