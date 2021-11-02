from itertools import zip_longest

import matplotlib.pyplot as plt
import matplotlib.colors
import seaborn as sns
import numpy as np
import json
import sys

from os.path import join
from os import listdir

def run(config, alg_name):
    print(f'Generating MAP-Elites graphs...')
    BASE_DIR = join(config.data_dir, alg_name)

    configs = []
    for file_name in listdir(BASE_DIR):
        if 'config' in file_name and '.json' in file_name and 'combined' not in file_name:
            f = open(join(BASE_DIR, file_name), 'r')
            configs.append(json.load(f))
            f.close()

    worst_performance = 1.0
    matrices = []
    for c in configs:
        resolution = c['resolution']
        matrix = [[np.nan for _ in range(resolution + 1)] for __ in range(resolution + 1)]

        f = open(c['data_file'])
        f.readline()
        content = f.readlines()
        f.close()

        for row in content:
            split_line = row.strip().split(',')
            worst_performance = max(worst_performance, float(split_line[3]))

            temp = matrix[int(split_line[1])][int(split_line[0])]
                
            if float(split_line[3]) == 0.0:
                if matrix[int(split_line[1])][int(split_line[0])] is np.nan:
                    matrix[int(split_line[1])][int(split_line[0])] = 0.0

                matrix[int(split_line[1])][int(split_line[0])] += 1
        
        num_elites = config.elites_per_bin
        assert num_elites > 0
        for y in range(resolution + 1):
            for x in range(resolution + 1):
                if not (matrix[y][x] is np.nan):
                    matrix[y][x] /= 4

        matrix = np.array(matrix)
        mask = np.zeros_like(matrix)
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == np.nan:
                    mask[i][j] = 1.0

        matrices.append(matrix)

    color_bar_label = 'Percent Elites Found Per Bin'
    cmap = 'Greens'

    for config, matrix in zip_longest(configs, matrices):
        x_dimensions, y_dimensions = config['feature_dimensions']
        resolution = int(config['resolution'])
        sns.set(rc={'figure.figsize':(11.7,8.27)})
        sns.color_palette('viridis')
        ax = sns.heatmap(
            matrix, 
            linewidths=.5, 
            square=True, 
            mask=mask,
            cmap=cmap,
            cbar_kws={'label': color_bar_label},
            vmin=0,
            vmax=1.0)

        ax.set(xlabel=config['x_label'], ylabel=config['y_label'])
        ax.set_xticks(ax.get_xticks()[::5])
        ax.set_yticks(ax.get_yticks()[::5])

        # lower dimension is always 0 so I'm being lazy
        xticks = [((x-0.5)/resolution) * x_dimensions[1] for x in ax.get_xticks().tolist()]
        yticks = [((y-0.5)/resolution) * y_dimensions[1] for y in ax.get_yticks().tolist()]
        ax.set_xticklabels(xticks)
        ax.set_yticklabels(yticks)

        ax.set(title=config['title'])
        ax.invert_yaxis()
        plt.savefig(config['save_file'], bbox_inches="tight")
        plt.close()
