from typing import List, Tuple, Callable
from Optimization.Operators import IMutate, ICrossover, IPopulationGenerator

class IConfig:
    def __init__(
        self, start_population_size: int, iterations: int, mutate: IMutate, 
        crossover: ICrossover, n_mutate: IMutate, n_crossover: ICrossover
    ):
        self.start_population_size = start_population_size
        self.iterations = iterations

        self.mutate = mutate
        self.crossover = crossover
        self.n_mutate = n_mutate
        self.n_crossover = n_crossover

    @property
    def data_dir(self) -> str:
        raise NotImplementedError()
    
    @property
    def feature_names(self) -> List[str]:
        raise NotImplementedError()
    
    @property
    def feature_dimensions(self) -> List[Tuple[float, float]]:
        raise NotImplementedError()
    
    @property
    def x_label(self) -> str:
        raise NotImplementedError()
    
    @property
    def y_label(self) -> str:
        raise NotImplementedError()
    
    @property
    def title(self) -> str:
        raise NotImplementedError()
    
    @property
    def feature_descriptors(self) -> List[Callable[[List[str]], float]]:
        raise NotImplementedError()
    
    @property
    def elites_per_bin(self) -> int:
        raise NotImplementedError()
    
    @property
    def resolution(self) -> int:
        raise NotImplementedError()
    
    @property
    def is_vertical(self) -> bool:
        raise NotImplementedError()
    
    @property
    def minimize_performance(self) -> bool:
        raise NotImplementedError()
    
    @property
    def start_strand_size(self) -> int:
        raise NotImplementedError()
    
    @property
    def max_strand_size(self) -> int:
        raise NotImplementedError()
    
    @property
    def mutation_values(self) -> List[str]:
        raise NotImplementedError()
    
    @property
    def population_generator(self) -> IPopulationGenerator:
        raise NotImplementedError()
    
    def fitness(self, lvl: List[str]) -> float:
        raise NotImplementedError()
    
    def level_to_str(self, lvl: List[str]) -> str:
        raise NotImplementedError()
