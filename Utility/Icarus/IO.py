from Config import Icarus
import os


def get_levels():
    levels = []

    for file_name in os.listdir(Icarus.data_dir):
        with open(os.path.join(Icarus.data_dir, file_name)) as f:
            levels.append([l.strip() for l in reversed(f.readlines())])

    return levels

def write_level(f, slices):
    f.write('\n'.join(reversed(slices)))
