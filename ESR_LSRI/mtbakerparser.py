import matplotlib.pyplot as pt
import numpy as np
import pandas as pd
import os

from statistics import stdev

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
    
def getiButtonData(site: str, desc: str, year: str):
    
    if desc not in ["Buried", "Shaded", "Exposed"] or year not in ["2018", "2019", "2020", "2021", "2022"]:
        raise Exception()
    return pd.read_csv("data//" + year + "//" + "MBCP" + year + "-" + str(int(year) + 1) + "_iButton" + getiButtonNum(site, desc, str(year)) + ".csv", skiprows=14, encoding="latin1")
    

def getAltitude(iButtonNum, year: str):
    
    if year not in ["2018", "2019", "2020", "2021", "2022"]:
        raise Exception()
    
    df = pd.read_csv("data//altitudes//altitudes" + year + ".csv", encoding="latin1")
    
    if not np.isnan(df.at[iButtonNum - 1, "Altitude (meters)"]):
        return df.at[iButtonNum - 1, "Altitude (meters)"]
    
    raise Exception("No altitude data.")

def toDecimalDate(date: str):
    try:
        x = date.split(" ")[0].split("/")
    except:
        raise Exception("failed" + str(date))
    
    return int(x[0])/13 + int(x[1])/365 + int(x[2])

                        
def getDataYears(site, desc, yrRange: str, ignoreMissingData: bool = True, returnTimes: bool = True) -> list:
    
    years = yrRange.split("-")
    data = []
    times = []
    
    num = years[0]

    while (int(num) < int(years[1])):

        try:
            data += getiButtonData(site, desc, num)["Value"].tolist()
            times += getiButtonData(site, desc, num)["Date/Time"].tolist()
        except:
            
            if not ignoreMissingData:
                raise Exception("Missing date from site {}, {}, {}, num {}.".format(site, desc, num, getiButtonNum(site, desc, num)))
                
        
        num = int(num) + 1
        num = str(num)
    if (returnTimes):
        return data, times
    return data

def difference(list1: list, list2: list) -> list:
    
    return [abs(a - b) for a, b in zip(list1, list2)]

#this function is hardcoded b/c doing it dynamically doesnt rlly matter
def graphExposedByHeight(path: str):
    
    figure, axis = pt.subplots(2, 3)
    
    axis[1][2].set_visible(False)
    
    figure.supxlabel("Decimal Date")
    figure.supylabel("Celcius")
    
    x = 0
    y = 0
    
    for folder in os.listdir(path):
        
        for file in os.listdir(path + folder):
            
            df = pd.read_csv(path + folder + "/" + file, skiprows = 14, encoding = 'latin1')
            axis[x][y].plot([toDecimalDate(x) for x in list(df.index.values)], df["Value"], label = folder)
            axis[x][y].legend(loc = 1)
            
            
            if y >= 2:
                x += 1
                y = 0
            else: y += 1

def listOf(num, size):
    return [num for x in range(size)]

def inRange(num1, num2, check):
    if check < num2 and check > num1:
        return True
    return False

def mean(list1):
    return sum(list1) / len(list1)

def removeOutliers(data, m=5, depth = 5):
    
    data1 = data
    
    for x in range(depth):
        data1 = data[abs(data - np.mean(data)) < m * np.std(data)]
        
    return data1
def graph(dfs, nums):
    
    prevFirst = 0.0
    prevLast = 100
    
    allDates = []
    allValues = []
   
    for ind, df in enumerate(dfs[::-1]):
        
        buried = whenBuried(df["Value"].to_list(), [round(toDecimalDate(x), 4) for x in list(df.index.values)])
        temp = list(removeOutliers(np.array(buried), m = 22.5, depth = 3))
        temp = buried[13:]
        
        #if (ind > 0):
          # temp = [x for x in temp if not prevFirst < x < prevLast]
        
        
        #prevFirst = temp[0]
        #prevLast = temp[-1]
        
        pt.scatter(temp, listOf(nums[ind], len(temp)), label = str(nums[ind]) + " (cm)", marker = "o")
        
        
        
        
        #allDates += temp
        #allValues += listOf(nums[ind], len(temp))
    
    
     
    


def f(x, *p):
    return np.poly1d(p)(x)
    

def getSnowDepth(path: str):
    
    dfs = []
    
    for folder in os.listdir(path):
        
        for file in os.listdir(path + folder):
            
            dfs.append(pd.read_csv(path + folder + "/" + file, skiprows = 14, encoding = 'latin1'))
    
    graph(dfs, [50, 100, 150, 200, 230][::-1])
    #print(whenBuried(dfs[0]["Value"].to_list(), [round(toDecimalDate(x), 4) for x in list(dfs[0].index.values)]))

def check(list1: list) -> bool:
    
    if stdev(list1) > 0.45:
        return False
    
    if (mean(list1) > 2):
        return False
    
    
    for num in list1:
        
        if not (-0.5 <= num <= 0.5):
        
            return False
    
    return True

def whenBuried(values: list, dates: list) -> list:
    
    prevDate = dates[0]
    dayData = []
    toReturn = []
    
    for ind, date in enumerate(dates):

        if date != prevDate:
            #check(): func to see if a sensor is buried based on list of day data
            if (check(dayData)):
                    toReturn.append(prevDate)
            prevDate = date
            dayData.clear()
        
        else:
            dayData.append(values[ind])
    return toReturn
            
    
    
            
            

path = "C:/Users/noahl/Desktop/ESR_LSRI-programs/dataorg/"
#inputs: site, description (Buried, Exposed, Shaded), year range, false to throw an exception when
#missing data, true to just ignore it

#data, times = getDataYears(1, "Buried","2018-2021", False)

#times = [round(toDecimalDate(x), 2) for x in times]

#graphExposedByHeight(path)
getSnowDepth(path)


pt.ylabel("Snow Height (cm)")
pt.xlabel("Decimal Date")
pt.legend()
pt.show()


    
    











