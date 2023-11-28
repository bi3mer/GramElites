from requests import post
from random import random

from Optimization.Operators.Mutate import Mutate
from Optimization.Operators.RandomPopulationGenerator import RandomPopulationGenerator
from Optimization.Operators.SinglePointCrossover import SinglePointCrossover

from typing import List, Tuple, Callable
from Optimization.Operators import IMutate, ICrossover, IPopulationGenerator

class IConfig:
    def __init__(self):
        self._mutation_values = [str(e) for e in range(7)]
        self._mutate = Mutate(self._mutation_values, 0.02)
        self._crossover = SinglePointCrossover()

        self._population_generator = RandomPopulationGenerator(
            self.start_strand_size, 
            self._mutation_values
        )

    def data_dir(self) -> str:
        return 'Match3Data'
    
    @property
    def start_population_size(self) -> int:
        return 500
    
    @property
    def iterations(self) -> int:
        return
    
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
    def mutate(self) -> IMutate:
        return self._mutate
    
    @property
    def crossover(self) -> ICrossover:
        return self._crossover
    
    # Match 3 doesn't implement gram-elites for now.
    # @property
    # def n_mutate(self) -> IMutate:
    #     raise NotImplementedError()
    
    # @property
    # def n_crossover(self) -> ICrossover:
    #     raise NotImplementedError()
    
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
        raise NotImplementedError()
    
    def fitness(lvl: List[str]) -> float:
        res = post('http://localhost:8000/solve', json=lvl)
        return int(res.content)
    
    def level_to_str(lvl: List[str]) -> str:
        return ','.join(str(e) for e in lvl)
