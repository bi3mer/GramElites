from Config import Mario, Icarus, DungeonGram

from time import time
import argparse
import sys

start = time()

parser = argparse.ArgumentParser(description='Level Generation Pipeline.')
parser.add_argument('--seed', type=int, default=0, help='Set seed for generation')
parser.add_argument(
    '--runs', 
    type=int,
    default=10,
    help='Set the # of runs. Walkthrough is the number of walks and average generates it the # of corpuses generated.')
parser.add_argument('--segments', type=int, default=3, help='set # of segments to be combined.')

game_group = parser.add_mutually_exclusive_group(required=True)
game_group.add_argument('--dungeongram', action='store_true', help='Run DungeonGrams')
game_group.add_argument('--mario', action='store_true', help='Run Mario')
game_group.add_argument('--icarus', action='store_true', help='Run Icarus')

type_group = parser.add_mutually_exclusive_group(required=True)
type_group.add_argument('--generate-corpus', action='store_true', help='Generate a corpus')
type_group.add_argument('--build_plots', action='store_true', help='Build plots from a corpus')
