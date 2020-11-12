import pandas as pd

soccer = pd.read_csv("/player_data_2020.csv")

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

soccer.corr()

plt.figure(figsize=(20, 20))

sns.heatmap( data = soccer.corr(), annot = True , )