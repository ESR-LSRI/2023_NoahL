import matplotlib.pyplot as pt
import numpy as np
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

def getiButtonNum(site, desc, year = "All"): #All: for debug purposes
    
    if desc not in ["Buried", "Shaded", "Exposed"] or year not in ["2018", "2019", "2020", "2021", "2022"]:
        raise Exception()
    
    if year == "All":
        return iButtons.iloc[getIndexFromDesc(site, desc)][2:]
    
  
    num = iButtons.at[getIndexFromDesc(site, desc), year + " #"] if not pd.isna(iButtons.at[getIndexFromDesc(site, desc), year + " #"]) else -1
    if (num == -1):
        raise Exception("No iButton for specified description.")
  
    return iButtons.at[getIndexFromDesc(site, desc), year + " #"]
    
def getiButtonData(site, desc, year: str):
    
    if desc not in ["Buried", "Shaded", "Exposed"] or year not in ["2018", "2019", "2020", "2021", "2022"]:
        raise Exception()
    try:
        return pd.read_csv("data//" + year + "//" + "MBCP" + year + "-" + str(int(year) + 1) + "_iButton" + getiButtonNum(site, desc, str(year)) + ".csv", skiprows=14, encoding="latin1")
    except:
        raise Exception("Missing data.")

def getAltitude(iButtonNum, year: str):
    
    if year not in ["2018", "2019", "2020", "2021", "2022"]:
        raise Exception()
    
    df = pd.read_csv("data//altitudes//altitudes" + year + ".csv", encoding="latin1")
    
    if not np.isnan(df.at[iButtonNum - 1, "Altitude (meters)"]):
        return df.at[iButtonNum - 1, "Altitude (meters)"]
    
    raise Exception("No altitude data.")

def getDataYears(site, desc, yrRange: str) -> list:
    
    years = yrRange.split("-")
    data = []
    
    print(years)
    
    num = years[0]

    while (True):

        data += getiButtonData(site, desc, num)["Value"].tolist()

        num = int(num) + 1
        num = str(num)
        
        if (int(num) > int(years[1])):
            
            break
    
    return data

pt.plot(getDataYears(1, "Buried", "2018-2021"))

pt.xlabel("Time")
pt.ylabel("Celcius")

pt.show()




    
    











