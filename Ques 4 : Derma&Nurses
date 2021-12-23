import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("C:/Users/AK/Downloads/datas.csv")

#droping all others except dermatologists and nurses

data.drop(data[(data["Spec Code"] != "06NRP") &
               (data["Spec Code"] != "06US") &
               (data["Spec Code"] != "01D") &
               (data["Spec Code"] != "01DDL") &
               (data["Spec Code"] != "01DMP") &
               (data["Spec Code"] != "01DS") &
               (data["Spec Code"] != "01PDD") &
               (data["Spec Code"] != "01PRD") &
               (data["Spec Code"] != "02D") &
               (data["Spec Code"] != "02DDL") &
               (data["Spec Code"] != "02DMP") &
               (data["Spec Code"] != "02DS") &
               (data["Spec Code"] != "02PDD") &
               (data["Spec Code"] != "02PRD") ]
               .index, inplace= True)

#dropping non FZO products

data= data.drop(data.index[data["Product Code"] == 1])

new_data = pd.DataFrame(data=data["Physician ID"])
new2 = pd.DataFrame(data=data[["Jan 2019","Feb 2019","Mar 2019","Apr 2019", "May 2019","Jun 2019","Jul 2019", "Aug 2019","Sep 2019", "Oct 2019","Nov 2019", "Dec 2019"]])
new2["Total"]=pd.DataFrame(data=new2.sum(axis=1))  
totf= pd.DataFrame(data=new2["Total"])

final = pd.concat([new_data,totf],axis=1)

final2 = final.groupby('Physician ID').sum()

final2["Decile_rank"] = pd.qcut(final2["Total"], 10, labels=False ,duplicates="drop")

final2


