import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("C:/Users/AK/Downloads/datas.csv")

#filling nulls with 0
data.fillna(value='0',inplace=True)

#dropping duplicates
data.drop_duplicates().shape
