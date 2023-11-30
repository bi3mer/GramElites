from typing import List
from .IConfig import IConfig

from Optimization.Operators import *
from Utility.Mario.IO import get_levels, level_to_str
from Utility.Mario.Behavior import *
from Utility.Mario.Fitness import *
from Utility import NGram
from Utility.LinkerGeneration import *

class Mario(IConfig):
    def __init__(self) -> None:
        START_STRAND_SIZE = 25

        n = 3
        self.gram = NGram(n)
        unigram = NGram(1)
        levels = get_levels()
        for level in levels:
            self.gram.add_sequence(level)
            unigram.add_sequence(level)

        unigram_keys = set(unigram.grammar[()].keys())
        pruned = self.gram.fully_connect()     # remove dead ends from grammar
        unigram_keys.difference_update(pruned) # remove any n-gram dead ends from unigram

        mutation_values = list(unigram_keys)

        super().__init__(
            start_population_size = 500,
            iterations = 80_000,
            data_dir = 'MarioData',
            feature_names = ['linearity', 'leniency'],
            feature_dimensions = [[0, 1], [0, 1]],
            feature_descriptors = [percent_linearity, percent_leniency],
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
            population_generator =  NGramPopulationGenerator(self.gram, START_STRAND_SIZE),
            mutate = Mutate(mutation_values, 0.02),
            crossover = SinglePointCrossover(),
            n_mutate = NGramMutate(0.02, self.gram, START_STRAND_SIZE),
            n_crossover = NGramCrossover(self.gram, START_STRAND_SIZE, START_STRAND_SIZE)
        )
    
    def fitness(self, lvl: List[str]) -> float:
        bad_n_grams = self.gram.count_bad_n_grams(lvl)
        return bad_n_grams + 1 - percent_playable(lvl)
    
    def level_to_str(self, lvl: List[str]) -> str:
        return level_to_str(lvl)