from city import City
from route import Route
import random
from copy import deepcopy
from typing import Set, Tuple, List, Sequence
import csv

CROSSOVER_POINT = 0.3
MUTATION_PROBABILITY = 0.5

def generate_cities(city_count: int, limit: Tuple[int, int]) -> Set[City]:
    cities = set()
    with open("cities.csv") as readable:
        reader = csv.reader(readable)
        for raw_city in reader:
            x = random.randint(0, limit[0])
            y = random.randint(0, limit[1])
            cities.add(City(name=raw_city[0], x=x, y=y))
    
    return random.sample(cities, city_count)
    

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

    crossover_point = int(CROSSOVER_POINT * len(child))
    for index_in_t, city_in_t in enumerate(parent_t[:3]):
        try:
            position_in_s = child.index(city_in_t)
            child[position_in_s] = child[index_in_t]
            child[index_in_t] = city_in_t
        except ValueError:
            import pdb; pdb.set_trace()
            pass
    return child



def crossover(routes: List[Route], population_size: int) -> List[Route]:
    missing_children = population_size - len(routes)
    new_children = []

    for _ in range(missing_children):
        parent1 = random.choice(routes)
        parent2 = random.choice(routes)
        
        while parent1 == parent2:
            # are parents allowed to mate with themselves?
            parent2 = random.choice(routes)

        new_route = Route(partially_mapped_crossover(parent1, parent2).data)
        new_children.append(new_route)
    return new_children


def _swap(route, to, frm):
        aux = route[to]
        route[to] = route[frm]
        route[frm] = aux


def mutate(routes: List[Route]) -> List[Route]:
    mutations = []
    for route in routes:
        new_route = deepcopy(route.data)
        if random.random() > MUTATION_PROBABILITY:
            swap_from = random.randint(0, len(route) -1)
            swap_to = random.randint(0, len(route) -1)
            _swap(new_route, swap_to, swap_from)
        mutations.append(Route(new_route))
    return mutations

    


