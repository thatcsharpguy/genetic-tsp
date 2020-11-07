import csv
import random
from copy import deepcopy
from typing import List, Sequence, Set, Tuple

from city import City
from route import Route

CROSSOVER_POINT = 0.6
MUTATION_PROBABILITY = 0.9


def generate_cities(
    city_count: int, minx: int, miny: int, maxx: int, maxy: int
) -> Set[City]:
    cities = set()
    with open("cities.csv", encoding="utf8") as readable:
        reader = csv.reader(readable)
        for raw_city in reader:
            x = random.randint(minx, maxx)
            y = random.randint(miny, maxy)
            cities.add(City(name=raw_city[0], x=x, y=y))

    return set(random.sample(cities, city_count))


def generate_population(cities: Set[City], population_size: int) -> List[Route]:
    population = []

    for _ in range(population_size):
        population.append(Route(random.sample(cities, len(cities))))

    return population


def select_parents(routes: List[Route], n_parents: int) -> List[Route]:
    ordered_by_distance = sorted(routes, key=lambda route: route.distance)
    return ordered_by_distance[:n_parents]


def partially_mapped_crossover(parent_s: Sequence, parent_t: Sequence):

    child = deepcopy(parent_s)

    crossover_qty = int(CROSSOVER_POINT * len(child))
    crossover_point = random.randint(0, len(child) - crossover_qty - 1)
    for index_in_t, city_in_t in enumerate(
        parent_t[crossover_point : crossover_point + crossover_point], crossover_point
    ):
        position_in_s = child.index(city_in_t)
        child[position_in_s] = child[index_in_t]
        child[index_in_t] = city_in_t
    return child


def crossover(routes: List[Route], population_size: int) -> List[Route]:
    missing_children = population_size - len(routes)
    new_children = []

    for _ in range(missing_children):
        parent1, parent2 = random.sample(routes, 2)

        new_route = Route(partially_mapped_crossover(parent1, parent2).data)
        new_children.append(new_route)
    return new_children


def _swap(route: Sequence, to: int, frm: int):
    aux = route[to]
    route[to] = route[frm]
    route[frm] = aux


def mutate(routes: List[Route]) -> List[Route]:
    mutations = []
    for route in routes:
        new_route = deepcopy(route.data)
        if MUTATION_PROBABILITY > random.random():
            swap_from = random.randint(0, len(route) - 1)
            swap_to = random.randint(0, len(route) - 1)
            while swap_to == swap_from:
                swap_to = random.randint(0, len(route) - 1)
            _swap(new_route, swap_to, swap_from)
        mutations.append(Route(new_route))
    return mutations
