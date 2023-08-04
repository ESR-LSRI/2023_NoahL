# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 09:21:20 2023
Graphs iButton data

@author: Noah L
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as pt
import sys

iButtons = pd.read_csv("data/iButtons.csv")
descLoc = {

    "Exposed": 0,
    "Buried": 1,
    "Shaded": 2

}


def getIndexFromDesc(site, desc):
    """
    Helper function that gets row of iButton in a Dataframe.
    
    Parameters
    ----------
    site : int
        site of iButton.
    desc : str
        type of iButton

    Returns
    -------
    int
        index of iButton.

    """
    return (site - 1) * 3 + descLoc[desc]

def getiButtonNum(site, desc, year="All"):  
    """
    
    Gets iButton number from site and description.

    Parameters
    ----------
    site : int
        Site of iButton.
    desc : str
        iButton description see descLoc for params.
    year : str, optional
        Year to get iButton num from. Default for debug purposes. The default is "All".

    Raises
    ------
    Exception
        When args are invalid.

    Returns
    -------
    int
        iButton number.

    """
    
    if desc not in ["Buried", "Shaded", "Exposed"] or year not in ["2018", "2019", "2020", "2021", "2022"]:
        raise Exception()

    if year == "All":
        return iButtons.iloc[getIndexFromDesc(site, desc)][2:]

    num = iButtons.at[getIndexFromDesc(site, desc), year + " #"] if not pd.isna(
        iButtons.at[getIndexFromDesc(site, desc), year + " #"]) else -1
    if (num == -1):
        raise Exception("No iButton for specified description.")

    return iButtons.at[getIndexFromDesc(site, desc), year + " #"]

def getDataYears(site, desc, yrRange: str, ignoreMissingData: bool = True, returnTimes: bool = True) -> list:
    """
    
    Gets data in a year range.

    Parameters
    ----------
    site : int
        Site of iButtons.
    desc : str
        iButton description.
    yrRange : str
        Range to get data from.
    ignoreMissingData : bool, optional
        False to throw an exception when missing data. Default to ignore. The default is True.
    returnTimes : bool, optional
        Debug purposes. Ignore. The default is True.

    Raises
    ------
    Exception
        Missing data if ignoreMissingData is false.

    Returns
    -------
    list, list
        data, times to plot.

    """
    
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
                raise Exception("Missing date from site {}, {}, {}, num {}.".format(
                    site, desc, num, getiButtonNum(site, desc, num)))
            else:
                
                
                times += [np.nan for x in np.arange(float(num) + 0.5, float(num) + 1.5)]
                data += [np.nan for x in np.arange(float(num) + 0.5, float(num) + 1.5)]
                

        num = int(num) + 1
        num = str(num)

    if (returnTimes):
        return data, times
    return data

def getiButtonData(site: str, desc: str, year: str):
    """
    Returns a dataframe of iButton data

    Parameters
    ----------
    site : str
        Site of iButton.
    desc : str
        iButton description.
    year : str
        Year to get iButton data from.

    Raises
    ------
    Exception
        Invalid params.

    Returns
    -------
    Dataframe
        Dataframe of iButton data

    """
    
    if desc not in ["Buried", "Shaded", "Exposed"] or year not in ["2018", "2019", "2020", "2021", "2022"]:
        raise Exception()
    return pd.read_csv("data//" + year + "//" + "MBCP" + year + "-" + str(int(year) + 1) + "_iButton" + getiButtonNum(site, desc, str(year)) + ".csv", skiprows=14, encoding="latin1")

def toDecimalDate(date, snotel=False):
    """
    Converts str to decimal date.
    
    Parameters
    ----------
    date : str
        date to convert
    snotel : bool, optional
        Ignore this param. The default is False.

    Returns
    -------
    num : int
        Decimal year.

    """
    if type(date) == str:
        if not snotel:
            try:
                x = date.split(" ")[0].split("/")
            except:
                raise Exception("failed" + str(date))
        else:
            x = date.split("/")

        num = (int(x[2])) + (((int(x[0])-1) * 30.4167 + int(x[1]))/365)
        num = num if snotel else num + 2000
        return num



if __name__ == "__main__":
    
    #for cmd args
    #data, times = getDataYears(int(sys.argv[1]), sys.argv[2], sys.argv[3], True)
    
    
    # inputs: site, description (Buried, Exposed, Shaded), year range, false to throw an exception when
    # missing data, true to just ignore it
    data, times = getDataYears(1, "Exposed", "2018-2020", True)
    timesParsed = []
    for x in times:
        
        try:
            
            timesParsed.append(round(toDecimalDate(x), 2))
            
        except:
            
            timesParsed.append(np.nan)
    
    pt.ylabel("Temperature (C)")
    pt.xlabel("Decimal Date")
    pt.ticklabel_format(style='plain', useOffset=False) 
    pt.plot(timesParsed, data)
    
    pt.show()

   

