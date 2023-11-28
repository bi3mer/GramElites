from typing import List, Tuple, Callable
from Optimization.Operators import IMutate, ICrossover, IPopulationGenerator

class IConfig:
    def data_dir(self) -> str:
        raise NotImplementedError()
    
    @property
    def start_population_size(self) -> int:
        raise NotImplementedError()
    
    @property
    def iterations(self) -> int:
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
    def mutate(self) -> IMutate:
        raise NotImplementedError()
    
    @property
    def crossover(self) -> ICrossover:
        raise NotImplementedError()
    
    @property
    def n_mutate(self) -> IMutate:
        raise NotImplementedError()
    
    @property
    def n_crossover(self) -> ICrossover:
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
    
    def fitness(lvl: List[str]) -> float:
        raise NotImplementedError()
    
    def level_to_str(lvl: List[str]) -> str:
        raise NotImplementedError()
