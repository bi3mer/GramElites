from requests import post
from random import random

from Optimization.Operators.Mutate import Mutate
from Optimization.Operators.RandomPopulationGenerator import RandomPopulationGenerator
from Optimization.Operators.SinglePointCrossover import SinglePointCrossover

data_dir = 'Match3Data'

start_population_size = 500
iterations = 100

feature_names = ['a', 'b']
feature_dimensions = [[0, 1], [0, 1]] 

x_label = 'temp1'
y_label = 'temp2'
title = 'Match 3'

def feature_a(lvl):
    return random() 

feature_descriptors = [feature_a, feature_a]

elites_per_bin = 4
resolution = 20

is_vertical = False

# Skipping n-gram stuff since it isn't relevant for this kind of puzzle.
n_mutate = None
n_crossover = None


minimize_performance = False # TODO: make true for later variant

start_strand_size = 6*7
max_strand_size = start_strand_size

mutation_values = list(range(7))

mutate = Mutate(mutation_values, 0.02)
crossover = SinglePointCrossover()

population_generator = RandomPopulationGenerator(start_strand_size, mutation_values)

def fitness(lvl):
    res = post('http://localhost:8000/solve', json=lvl)
    return int(res.content)

def level_to_str(lvl):
    return ','.join(str(e) for e in lvl)
