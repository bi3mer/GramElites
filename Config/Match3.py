from requests import post
from random import random
from typing import List

from Optimization.Operators.Mutate import Mutate
from Optimization.Operators.RandomPopulationGenerator import RandomPopulationGenerator
from Optimization.Operators.SinglePointCrossover import SinglePointCrossover

from .Icarus import IConfig

class Match3(IConfig):
    def __init__(self):
        START_STRAND_SIZE = 42 # 6 (columns) * 7 (rows)
        mutation_values = [str(e) for e in range(7)]

        super().__init__(
            start_population_size = 100,
            iterations = 100,
            data_dir = 'Match3Data',
            feature_names = ['A', 'B'],
            feature_dimensions = [[0, 1], [0, 1]],
            feature_descriptors = [lambda lvl: random(), lambda lvl: random()],
            x_label = 'Density',
            y_label = 'Leniency',
            title = '',
            elites_per_bin = 4,
            resolution = 40,
            is_vertical = False,
            start_strand_size = START_STRAND_SIZE,
            max_strand_size = START_STRAND_SIZE,
            minimize_performance = True,
            mutation_values = mutation_values,
            population_generator =  RandomPopulationGenerator(START_STRAND_SIZE, mutation_values),
            mutate = Mutate(mutation_values, 0.02),
            crossover = SinglePointCrossover(),
            n_mutate = None,   # Match 3 doesn't implement gram-elites
            n_crossover = None # Match 3 doesn't implement gram-elites
        )

    def fitness(self, lvl: List[str]) -> float:
        res = post('http://localhost:8000/solve', json=[int(e) for e in lvl])
        return int(res.content)
    
    def level_to_str(self, lvl: List[str]) -> str:
        return ','.join(str(e) for e in lvl)
