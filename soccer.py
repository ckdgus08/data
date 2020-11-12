import pandas as pd

soccer = pd.read_csv("player_data_2020.csv")

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

soccer.corr()

print(sns.heatmap( data = soccer.corr(), annot = True ))