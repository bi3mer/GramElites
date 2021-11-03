# Gram-Elites

A free to read version of the paper can be found [here](https://bi3mer.github.io/pdf/2021_gram_elites.pdf).

## Abstract

In the context of procedural content generation via machine learning (PCGML), quality-diversity (QD) algorithms are a powerful tool to generate diverse game content. A branch of QD uses genetic operators to generate content (e.g. MAP-Elites). Problematically, levels generated with these operators have no guarantee of matching the style of a game. This can be addressed by incorporating whether a level is generable by an n-gram into the fitness function. Unfortunately, this leads to wasted computation and poor results. In this work, we introduce n-gram genetic operators, which produce only solutions that are generable by the n-gram model; we call MAP-Elites combined with these operators Gram-Elites. We test on a tile-based side-scrolling platformer, vertical platformer, and roguelike. For all three, n-gram operators outperform standard operators and random n-gram generation, finding more usable (i.e. completable and generable) solutions at a faster rate. By integrating structure into operators, instead of fitness, these genetic operators could be beneficial to QD in PCGML.

## Use


GAME can be "mario", "icarus", or "dungeongram". ALGORITHM can be "n-gram-placement", "map-elites", or "gram-elites".

*Generate a levels*
```bash
pypy3 main.py --{GAME} --{ALGORITHM} --generate-corpus
```

*Plot the MAP-Elites grid*
```bash
python3 main.py --{GAME} --{ALGORITHM} --plot-map-elites
```

*Run level generation multiple times*
```bash
pypy3 main.py --{GAME} --{ALGORITHM} --average-generated --runs {n}
```

*Plot average generated*
```bash
python3 main.py --{GAME} --{ALGORITHM} --plot-counts
```


## Citation

```
@inproceedings{biemer2021gram,
  title={Gram-Elites: N-Gram Based Quality-Diversity Search},
 author={Colan Biemer and Alejandro Hervella and Seth Cooper},
 booktitle={Proceedings of the FDG workshop on Procedural Content Generation},
 year={2021}
}
```
