import matplotlib.pyplot as pt
import numpy as np
import pandas as pd
import os

from scipy import stats
from statistics import stdev

descLoc = {

    "Exposed": 0,
    "Buried": 1,
    "Shaded": 2

}

iButtons = pd.read_csv("alldata/data/iButtons.csv")


def getIndexFromDesc(site, desc):

    return (site - 1) * 3 + descLoc[desc]


def getiButtonNum(site, desc, year="All"):  # All: for debug purposes

    if desc not in ["Buried", "Shaded", "Exposed"] or year not in ["2018", "2019", "2020", "2021", "2022"]:
        raise Exception()

    if year == "All":
        return iButtons.iloc[getIndexFromDesc(site, desc)][2:]

    num = iButtons.at[getIndexFromDesc(site, desc), year + " #"] if not pd.isna(
        iButtons.at[getIndexFromDesc(site, desc), year + " #"]) else -1
    if (num == -1):
        raise Exception("No iButton for specified description.")

    return iButtons.at[getIndexFromDesc(site, desc), year + " #"]


def getiButtonData(site: str, desc: str, year: str):

    if desc not in ["Buried", "Shaded", "Exposed"] or year not in ["2018", "2019", "2020", "2021", "2022"]:
        raise Exception()
    return pd.read_csv("alldata//data//" + year + "//" + "MBCP" + year + "-" + str(int(year) + 1) + "_iButton" + getiButtonNum(site, desc, str(year)) + ".csv", skiprows=14, encoding="latin1")


def getAltitude(iButtonNum, year: str):

    if year not in ["2018", "2019", "2020", "2021", "2022"]:
        raise Exception()

    df = pd.read_csv("alldata//data//altitudes//altitudes" +
                     year + ".csv", encoding="latin1")

    if not np.isnan(df.at[iButtonNum - 1, "Altitude (meters)"]):
        return df.at[iButtonNum - 1, "Altitude (meters)"]

    raise Exception("No altitude data.")


def toDecimalDate(date, snotel=False):

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

    else:

        x = date
        return (int(x[0])) + (((int(x[1])-1) * 30.4167 + int(x[2]))/365)


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


def difference(list1: list, list2: list) -> list:

    return [abs(a - b) for a, b in zip(list1, list2)]

# this function is hardcoded b/c doing it dynamically doesnt rlly matter


def graphExposedByHeight(path: str):

    figure, axis = pt.subplots(2, 3)

    axis[1][2].set_visible(False)

    figure.supxlabel("Decimal Date")
    figure.supylabel("Celcius")

    x = 0
    y = 0

    for folder in os.listdir(path):

        for file in os.listdir(path + folder):

            df = pd.read_csv(path + folder + "/" + file,
                             skiprows=14, encoding='latin1')
            axis[x][y].plot([toDecimalDate(x) for x in list(
                df.index.values)], df["Value"], label=folder)
            axis[x][y].legend(loc=1)

            if y >= 2:
                x += 1
                y = 0
            else:
                y += 1


def listOf(num, size):
    return [num for x in range(size)]


def inRange(num1, num2, check):
    if check < num2 and check > num1:
        return True
    return False


def mean(list1):
    return sum(list1) / len(list1)


def calcZScoreWithMean(list1, val, mean):
    return (val - mean) / stdev(list1)


def zScore(list1, mean):

    if mean == None:
        return [round(x, 4) for x in stats.zscore(list1)]
    else:
        return [round(calcZScoreWithMean(list1, x, mean), 4) for x in list1]


def removeOutliersZ(list1, thresholdb, thresholdt, mean):

    removed = [x for x, y in zip(list1, zScore(
        list1, mean)) if thresholdb < y < thresholdt]
    return removed


def npdt64ToStr(date):

    return str(date).split("T")[0].replace("-", "/").split("/")


def removeOutliersQuartile(list1):

    list1 = np.array(list1)

    Q1 = np.percentile(list1, 25)
    Q3 = np.percentile(list1, 75)

    IQR = Q3 - Q1

    upper = Q3 + 1.5*IQR
    lower = Q1 - 1.5*IQR

    upper_array = np.where(list1 >= upper)[0]
    lower_array = np.where(list1 <= lower)[0]

    for x, y in zip(upper_array, lower_array):

        list1.pop(x)
        list1.pop(y)

    return list(list1)


def graph(dfs, nums, removeOutliers=False):

    #allDates = []
    #allValues = []
    prevTemp = []
    temp = []

    for en, df in enumerate(dfs[::-1]):

        if not type(df.index.values[0]) == np.datetime64:
            buried = whenBuried(df["Value"].to_list(), [round(
                toDecimalDate(x), 4) for x in list(df.index.values)])

        else:
            buried = whenBuried(df["Value"].to_list(), [round(
                toDecimalDate(npdt64ToStr(x)), 2) for x in list(df.index.values)])

        #temp += removeOutliersZ(buried[4:], -1, 1, mean(buried[4:]))
        #temp += removeOutliersQuartile(buried[4:])
        #temp += buried[7:]
        temp += buried

        if en % 2 == 1:

            if df is dfs[0]:
                pt.scatter(temp, listOf(
                    nums[en // 2], len(temp)), color="red", label="iButton data")

            else:
                pt.scatter(temp, listOf(nums[en // 2], len(temp)), color="red")

            temp.clear()

        """
        if (outsideOnly):
            if (ind > 0):
                temp += buried[7:9] + buried[-9:-7]
            else:
                temp += buried[8:]
        else:
            temp = buried[7:-2]

        if ind % 2 == 1:
            print("hi")
            pt.scatter(temp, listOf(nums[ind], len(temp)), label=str(
                nums[ind]) + " (cm)", marker="o")
            temp = []

        allDates += temp
        allValues += listOf(nums[ind], len(temp))
        
        if (en % 2 == 1):
            ind += 1;
        """


def getSnowDepth(path: str, outsideOnly=False):

    dfs = []

    for folder in os.listdir(path):

        for file in os.listdir(path + folder):

            if file.split(".")[-1] == "csv":
                dfs.append(pd.read_csv(path + folder + "/" +
                           file, skiprows=14, encoding='latin1'))
            else:
                df = pd.read_pickle(path + folder + "/" + file)

                dfs.append(df)
                """
                df.reset_index(inplace=True)
                df = df.rename(columns = {'index':'date'})
                
                dfs.append(df)
                """
    graph(dfs, [50, 100, 150, 200, 230][::-1], outsideOnly)
    #print(whenBuried(dfs[0]["Value"].to_list(), [round(toDecimalDate(x), 4) for x in list(dfs[0].index.values)]))


def check(list1: list) -> bool:

    if stdev(list1) < 0.45:
        return True

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
            # check(): func to see if a sensor is buried based on list of day data
            if (check(dayData)):
                toReturn.append(prevDate)
            prevDate = date
            dayData.clear()

        else:
            dayData.append(values[ind])
    return toReturn


def graphSnotelData(path: str, site: str, cHex: str, typeGraph: str) -> None:

    dfs = [pd.read_csv(path + site + "_25_YEAR=2022" + ".csv", encoding="latin1", skiprows=2),
           pd.read_csv(path + site + "_25_YEAR=2021" +
                       ".csv", encoding="latin1", skiprows=2),
           pd.read_csv(path + site + "_25_YEAR=2023" + ".csv", encoding="latin1", skiprows=2)]

    totalv = []
    totalt = []

    for ind, df in enumerate(dfs):
       # print(ind)

        values = df.iloc[:, 3].to_list()
        times = df["Date"].to_list()

        totalv += [x * 2.54 for x in values]
        totalt += [round(toDecimalDate(x, True), 2) for x in times]

    if (typeGraph == "s"):
        pt.scatter(totalt, totalv, color=cHex, label="SNOTEL data " + site)
    else:
        pt.plot(totalt, totalv, color=cHex, label="SNOTEL data " + site)


# inputs: site, description (Buried, Exposed, Shaded), year range, false to throw an exception when
# missing data, true to just ignore it
data, times = getDataYears(1, "Buried", "2018-2021", True)
timesParsed = []
for x in times:
    
    try:
        
        timesParsed.append(round(toDecimalDate(x), 2))
        
    except:
        
        timesParsed.append(np.nan)

pt.plot(timesParsed, data)


path = "alldata/dataorg/"
pathSnotel = "alldata/snoteldata/"
# graphExposedByHeight(path)
# graphSnotelData(pathSnotel, "999", "#000000", "s")
# graphSnotelData(pathSnotel, "910", "#800080", "s")
#getSnowDepth(path, False)


pt.ylabel("Snow Height (cm)")
pt.xlabel("Decimal Date")
#pt.xlim(2021.75, 2023.5)
#pt.ylim(-200, 500)

pt.legend()
pt.show()
