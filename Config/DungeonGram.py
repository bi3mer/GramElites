from typing import List, Callable, Tuple
from .IConfig import IConfig

from dungeongrams.dungeongrams import *
from Optimization.Operators import *
from Utility.DungeonGram.IO import get_levels, level_to_str
from Utility.DungeonGram.Behavior import *
from Utility import NGram
from Utility.GridTools import columns_into_rows
from Utility.LinkerGeneration import *

from dungeongrams import *

class DungeonGram(IConfig):
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

        super().__init__(
            50,
            50, # 60_000
            Mutate(self._mutation_values, 0.02),
            SinglePointCrossover(),
            NGramMutate(0.02, self.gram, self.max_strand_size),
            NGramCrossover(self.gram, self.start_strand_size, self.max_strand_size)
        )

    @property
    def data_dir(self) -> str:
        return 'DungeonData'
    
    @property
    def feature_names(self) -> List[str]:
        return ['density', 'leniency']
    
    @property
    def feature_dimensions(self) -> List[Tuple[float, float]]:
        return [[0, 1], [0, 0.5]] 
    
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
        return 20
    
    @property
    def is_vertical(self) -> bool:
        return False
    
    @property
    def minimize_performance(self) -> bool:
        return True
    
    @property
    def start_strand_size(self) -> int:
        return 15
    
    @property
    def max_strand_size(self) -> int:
        return 15
    
    @property
    def mutation_values(self) -> List[str]:
        return self._mutation_values
    
    @property
    def population_generator(self) -> IPopulationGenerator:
        return self._population_generator
    
    def __get_percent_playable(self, level, thorough=False, agent=None):
        if agent == None:
            agent = FLAW_NO_FLAW

        return percent_playable(columns_into_rows(level), False, True, thorough, agent)
    
    def fitness(self, lvl: List[str]) -> float:
        bad_n_grams = self.gram.count_bad_n_grams(lvl)
        return bad_n_grams + 1 - self.__get_percent_playable(lvl)
    
    def level_to_str(self, lvl: List[str]) -> str:
        return level_to_str(lvl)