import matplotlib.pyplot as pt
import numpy as np
import os as os
import pandas as pd

from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

descLoc = {
    
    "Exposed": 0,
    "Buried": 1,
    "Shaded": 2
    
}

iButtons = pd.read_csv("data//iButtons.csv")

def getIndexFromDesc(site, desc):
    
    return (site - 1) * 3 + descLoc[desc]

def getiButtonNum(site, desc, year = "All"):
    
    if desc not in ["Buried", "Shaded", "Exposed"] or year not in ["2018", "2019", "2020", "2021", "2022"]:
        raise Exception()
    
    if year == "All":
        return iButtons.iloc[getIndexFromDesc(site, desc)][2:]
    
    
    num = iButtons.at[getIndexFromDesc(site, desc), year + " #"] if not np.isnan(iButtons.at[getIndexFromDesc(site, desc), year + " #"]) else -1
    if (num == -1):
        raise Exception("No iButton for specificed description.")
    
    return num
    
def getiButtonData(site, desc, year: str):
    
    if desc not in ["Buried", "Shaded", "Exposed"] or year not in ["2018", "2019", "2020", "2021", "2022"]:
        raise Exception()
    
    return pd.read_csv("data//" + year + "//" + "MBCP" + year + "-" + str(int(year) + 1) + "_iButton" + getiButtonNum(site, desc, str(year)) + ".csv", skiprows=14)
        

def getAltitude(iButtonNum, year: str):
    
    if year not in ["2018", "2019", "2020", "2021", "2022"]:
        raise Exception()
    
    df = pd.read_csv("data//altitudes//altitudes" + year + ".csv")
    
    if not np.isnan(df.at[iButtonNum - 1, "Altitude (meters)"]):
        return df.at[iButtonNum - 1, "Altitude (meters)"]
    
    raise Exception("No altitude data.")
    





    
    











