import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("C:/Users/AK/Downloads/datas.csv")



new_data = pd.DataFrame(data=data[["Physician ID"," State"]])

new2 = pd.DataFrame(data=data[["Jan-19","Feb-19","Mar-19","Apr-19", "May-19","Jun-19","Jul-19", "Aug-19","Sep-19", "Oct-19","Nov-19", "Dec-19"]])
 
new_data["Total"] = new2.sum(axis=1)

final2 = new_data.groupby(' State').sum()

rank=final2.sort_values(by="Total",ascending=False)

rank = rank.plot(y=["Total"],kind = 'bar',title='Market Share of Different Sates',figsize=(15,5))
rank.set_xlabel("States")
rank.set_ylabel("MarketShare")

