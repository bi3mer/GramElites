from requests import post
from random import random

from Optimization.Operators.Mutate import Mutate
from Optimization.Operators.RandomPopulationGenerator import RandomPopulationGenerator
from Optimization.Operators.SinglePointCrossover import SinglePointCrossover

from typing import List, Tuple, Callable
from Optimization.Operators import IPopulationGenerator
from .Icarus import IConfig

class Match3(IConfig):
    def __init__(self):
        self._mutation_values = [str(e) for e in range(7)]
        self._population_generator = RandomPopulationGenerator(
            self.start_strand_size, 
            self._mutation_values
        )

        super().__init__(
            100,
            100,
            Mutate(self._mutation_values, 0.02),
            SinglePointCrossover(),
            None, # Match 3 doesn't implement gram-elites
            None  # Match 3 doesn't implement gram-elites
        )

    @property
    def data_dir(self) -> str:
        return 'Match3Data'
    
    @property
    def feature_names(self) -> List[str]:
        return ['a', 'b']
    
    @property
    def feature_dimensions(self) -> List[Tuple[float, float]]:
        return [[0, 1], [0, 1]] 
    
    @property
    def x_label(self) -> str:
        return 'x'
    
    @property
    def y_label(self) -> str:
        return 'y'
    
    @property
    def title(self) -> str:
        return 'Match 3'
    
    @property
    def feature_descriptors(self) -> List[Callable[[List[str]], float]]:
        return [lambda lvl: random(), lambda lvl: random()]
    
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
        return False
    
    @property
    def start_strand_size(self) -> int:
        return 42 # 6 (columns) * 7 (rows)
    
    @property
    def max_strand_size(self) -> int:
        return 42 # see above
    
    @property
    def mutation_values(self) -> List[str]:
        return self._mutation_values
    
    @property
    def population_generator(self) -> IPopulationGenerator:
        return self._population_generator
    
    def fitness(self, lvl: List[str]) -> float:
        res = post('http://localhost:8000/solve', json=[int(e) for e in lvl])
        return int(res.content)
    
    def level_to_str(self, lvl: List[str]) -> str:
        return ','.join(str(e) for e in lvl)
