from tkinter import BOTH, CENTER, NW, SUNKEN, Canvas, Frame, Label, StringVar, Tk, W, messagebox
from timeit import default_timer as timer
from datetime import timedelta
import threading as threading
import multiprocessing as mp
from route import Route
from city import City
from population_utils import (
    _swap,
    crossover,
    generate_cities,
    generate_population,
    mutate,
    partially_mapped_crossover,
    select_parents,
)

window_width = 1000
window_height = 800
n_cities = 20
population_size = 100
parents_size = 50
max_generations = 500

window_padding = 10
current_generation = 0
cities = generate_cities(
    n_cities,
    minx=window_padding,
    maxx=window_width - window_padding,
    miny=window_padding,
    maxy=window_height - window_padding,
)
population = generate_population(cities, population_size)

class CityMapper(Frame):
    def __init__(self):
        super().__init__()

        self.master.title("Travelling Pokemon Trainer Problem")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        self.text = StringVar()
        self.statusbar = Label(
            self, textvariable=self.text, bd=1, relief=SUNKEN, anchor=W
        )

    def draw_city(self, x, y, name, **kwargs):
        '''
        Pokemon colors 
        Yellow: #ffde00, Cerulean Blue: #3b4cca, Dark blue: #003a70
        '''

        r = 5
        self.canvas.create_oval(
            x - r, y - r, x + r, y + r, fill="#003a70", outline="#3b4cca", width=3
        )
        self.canvas.create_text(
            x, y - 10, anchor=CENTER, font=("Open Sans", 9), text=name
        )

    def draw_best_ui(self, cities, route, generation):

        self.canvas.delete("all")

        self.canvas.create_text(
            5,
            0,
            anchor=NW,
            font=("Open Sans", 18),
            text=f"Generation {generation:03} \nDistance: {route.distance:.3f}",
        )
        for a, b in zip(route[1:], route[:-1]):
            self.canvas.create_line(a.x, a.y, b.x, b.y, fill="#ffde00", width=3)
        for city in cities:
            self.draw_city(city.x, city.y, city.name)
        self.canvas.pack(fill=BOTH, expand=1)


def genetic_algorithm(example, root):
    global population
    global current_generation

    start_time = timer()
    
    best_routes = sorted(population, key=lambda route: route.distance)

    example.draw_best_ui(cities, best_routes[0], current_generation)
    parents = select_parents(population, parents_size)
    new_children = crossover(parents, population_size)

    new_children_mutated = mutate(new_children)

    population = parents + new_children_mutated

    if current_generation == max_generations:
        end_time = timer()
        final_time = end_time - start_time
        message = "Current generation " + str(current_generation) + "\n Time {}".format(timedelta(seconds=final_time))
        messagebox.showinfo("Done!", message)
    else:
        root.after(100, genetic_algorithm, example, root)
    current_generation = current_generation + 1


def main():

    root = Tk()
    app = CityMapper()
    root.geometry(f"{window_width}x{window_height}")
    root.after(100, genetic_algorithm, app, root)
    root.mainloop()


if __name__ == "__main__":
    main()
