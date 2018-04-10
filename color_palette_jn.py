import numpy as np

def colors_palette():
    """
    :return: array with rgb values
    """
    return np.array([
        [0.1, 0.1, 0.1],          # black
        [0.3, 0.3, 0.3],          # dark gray
        [0.6, 0.6, 0.6],          # gray
        [0.8, 0.8, 0.8],          # light gray
        [1.0, 0.827, 0.067],      # dark yellow
        [0.698, 0.063, 0.02],     # dark red
        [0.004, 0.6, 0.153],      # dark green
        [0.2, 0.666, 0.866],      # medium light blue
        [0.024, 0.412, 0.64]      # dark blue
    ])
