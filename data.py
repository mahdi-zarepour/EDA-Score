import statistics as st
import os

import pandas as pd
import numpy as np


data = {
    'AS': [
        10, 8.5, 9.5, 10, 9, 10, 4.5, 3.5, 3.5, 9, 7.5, 9, 3, 10, 10, 5, 9, 7, 0.5,
        7.75, 2.5, 8, 10, 9, 2.5, 6,
    ],
    'AP': [
        2.5, 3.5, 2.5, 7, 2.25, 7.5, 6.25, 2.5, 1, 3.5, 6.25, 1, 0, 7.5, 0,
        2.75, 6.75, 6.5, 0, 2.5, 2, 2.5, 2.5, 5, 2, 4,
    ],
    'BS': [
        0, 8, 1.75, 0.5, 2, 8.5, 8.5, 10, 1.25, 7.5, 4.75, 8.5, 6, 7.5, 7,
        8.5, 7.5, 8.5, 8.5, 7.5, 7.5, 5, 10, 8.5, 8, 7.5,
    ],
    'BP': [
        0.5, 2.25, 4.5, 1.25, 0.5, 1, 7.25, 8.75, 1.25, 2.25, 0, 0.75, 2.25,
        1.25, 2.5, 6.75, 1.25, 2, 7.5, 1.5, 1.75, 2.5, 3, 7.5, 1, 3.5,
    ],
}

df = pd.DataFrame(data)
df.to_csv(f'{os.path.dirname(__file__)}\score.csv')
