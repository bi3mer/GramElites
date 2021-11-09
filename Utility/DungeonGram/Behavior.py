from .config import *

def density(columns):
    num_solid_blocks = 0
    total_number_of_blocks = 0
    for col in columns:
        num_solid_blocks += col.count(SOLID_BLOCK)
        num_solid_blocks += col.count(STRUCTURE_1)
        num_solid_blocks += col.count(STRUCTURE_2)
        total_number_of_blocks += len(col)

    return num_solid_blocks / total_number_of_blocks

def leniency(columns):
    count = 0
    for col in columns:
        if SPIKE in col :
            count += 1/3
        if ENEMY in col:
            count += 1/3
        if SWITCH in col:
            count += 1/3

    return count / len(columns)
