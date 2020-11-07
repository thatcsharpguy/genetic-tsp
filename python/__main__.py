from population_utils import generate_cities, partially_mapped_crossover, generate_population, select_parents, crossover, mutate

from population_utils import _swap
from route import Route
from city import City

"""
import random

n_cities = 100
population_size = 100
parents_size = 50
max_generations = 100

cities = generate_cities(n_cities, (20,20))
population = generate_population(cities, population_size)


for generation in range(max_generations):

    parents = select_parents(population, parents_size)
    new_children = crossover(parents, population_size)

    new_children_mutated =  mutate(new_children)

    population = parents + new_children_mutated
    best_routes = sorted(population, key = lambda route: route.distance)

    print(best_routes[0].distance)
"""


from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_line(15, 25, 200, 25)
        canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)

        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Example()
    root.geometry("400x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()