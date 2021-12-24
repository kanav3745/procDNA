import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("C:/Users/AK/Downloads/datas.csv")

#seprating dermatologists and nurses data

nurse_data = pd.DataFrame(data[
               (data["Spec Code"] == "06NRP") |
               (data["Spec Code"] == "06US")               
               ])

derma_data = pd.DataFrame(data[
               (data["Spec Code"] == "01D") |
               (data["Spec Code"] == "01DDL") |
               (data["Spec Code"] == "01DMP") |
               (data["Spec Code"] == "01DS") |
               (data["Spec Code"] == "01PDD") |
               (data["Spec Code"] == "01PRD") |
               (data["Spec Code"] == "02D") |
               (data["Spec Code"] == "02DDL")|
               (data["Spec Code"] == "02DMP") |
               (data["Spec Code"] == "02DS") |
               (data["Spec Code"] == "02PDD") |
               (data["Spec Code"] == "02PRD") 
               ])



#Summing up total prescriptions for dermatologists
tpd = pd.DataFrame(data=derma_data[["Jan 2019","Feb 2019","Mar 2019","Apr 2019", "May 2019","Jun 2019","Jul 2019", "Aug 2019","Sep 2019", "Oct 2019","Nov 2019", "Dec 2019"]])
tpd["Total"]=pd.DataFrame(data=tpd.sum(axis=1))  

total=pd.DataFrame(data=tpd["Total"])
dt = pd.DataFrame(data=total.sum(axis=0))
dt.columns=["Dermatologist_total_prescriptions"]

#Summing up total prescriptions for nurses
tpn = pd.DataFrame(data=nurse_data[["Jan 2019","Feb 2019","Mar 2019","Apr 2019", "May 2019","Jun 2019","Jul 2019", "Aug 2019","Sep 2019", "Oct 2019","Nov 2019", "Dec 2019"]])
tpn["Total"]=pd.DataFrame(data=tpn.sum(axis=1))  

total2=pd.DataFrame(data=tpn["Total"])
nt = pd.DataFrame(data=total2.sum(axis=0))
dt["Nurse_total_prescriptions"]=nt

#comparing both
dt
