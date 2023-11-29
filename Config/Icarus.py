from typing import List, Tuple, Callable
from .IConfig import IConfig

from Optimization.Operators import *
from Utility.Icarus.IO import get_levels, level_to_str
from Utility.Icarus.Behavior import *
from Utility.Icarus.Fitness import *
from Utility import NGram
from Utility.LinkerGeneration import *

class Icarus(IConfig):
    def __init__(self) -> None:
        n = 2
        self.gram = NGram(n)
        unigram = NGram(1)
        levels = get_levels()
        for level in levels:
            self.gram.add_sequence(level)
            unigram.add_sequence(level)

        unigram_keys = set(unigram.grammar[()].keys())
        pruned = self.gram.fully_connect()     # remove dead ends from grammar
        unigram_keys.difference_update(pruned) # remove any n-gram dead ends from unigram

        self._mutation_values = list(unigram_keys)
        self._population_generator = NGramPopulationGenerator(self.gram, self.start_strand_size)

        self.__percent_completable = build_slow_fitness_function(self.gram)

        super().__init__(
            500,
            120_000,
            Mutate(self._mutation_values, 0.02),
            SinglePointCrossover(),
            NGramMutate(0.02, self.gram, self.max_strand_size),
            NGramCrossover(self.gram, self.start_strand_size, self.max_strand_size)
        )

    @property
    def data_dir(self) -> str:
        return 'IcarusData'
    
    @property
    def feature_names(self) -> List[str]:
        return ['density', 'leniency']
    
    @property
    def feature_dimensions(self) -> List[Tuple[float, float]]:
        return [[0, 1], [0, 1]] 
    
    @property
    def x_label(self) -> str:
        return 'Linearity'
    
    @property
    def y_label(self) -> str:
        return 'Leniency'
    
    @property
    def title(self) -> str:
        return ''
    
    @property
    def feature_descriptors(self) -> List[Callable[[List[str]], float]]:
        return [density, leniency]
    
    @property
    def elites_per_bin(self) -> int:
        return 4
    
    @property
    def resolution(self) -> int:
        return 40
    
    @property
    def is_vertical(self) -> bool:
        return True
    
    @property
    def minimize_performance(self) -> bool:
        return True
    
    @property
    def start_strand_size(self) -> int:
        return 25
    
    @property
    def max_strand_size(self) -> int:
        return 25
    
    @property
    def mutation_values(self) -> List[str]:
        return self._mutation_values
    
    @property
    def population_generator(self) -> IPopulationGenerator:
        return self._population_generator
    
    def fitness(self, lvl: List[str]) -> float:
        bad_n_grams = self.gram.count_bad_n_grams(lvl)
        return bad_n_grams + 1 - self.__percent_completable(lvl)
    
    def level_to_str(self, lvl: List[str]) -> str:
        return level_to_str(lvl)