import matplotlib.pyplot as pt
import numpy as np
import os as os
import pandas as pd

from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

site: int = 1
year: str = "2018 #"
description: str = "Exposed"

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
    
    return iButtons.at[getIndexFromDesc(site, desc), year + " #"]

#Allows me to get the iButton number based on site, description, and year. will be useful for getting the correct iButton number when getting data from files.
print(getiButtonNum(1, "Exposed", "2021"))


    
    











