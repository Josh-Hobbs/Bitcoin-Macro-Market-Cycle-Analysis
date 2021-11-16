import pandas as pd
import matplotlib.pyplot as plt
import os
import datetime as dt
import matplotlib.animation as animation

#Importing/Reading the price data from CSV file
data = pd.read_csv("bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv")
Timestamp = pd.to_datetime(data["Timestamp"],unit="s")

data = data.dropna()
data.reset_index(inplace=True, drop=True)

data["Timestamp"] = pd.to_datetime(data["Timestamp"],unit='s')

data["Year"] = pd.DatetimeIndex(data["Timestamp"]).year

fig, ax = plt.subplots()

data["Day"] =  pd.DatetimeIndex(data["Timestamp"]).day
data["Month"] = pd.DatetimeIndex(data["Timestamp"]).month

#Pulling price data from each cycle and finding the ROI increase/decrease for each price data point
#Plots each ROI in the cycle and labels the maximum ROI for the cycle

def Cycle1():
    Close2011to2012 = data.loc[1:312000,["Close","Year"]]
    CycleTwoYs = Close2011to2012["Close"].tolist()
    CycleTwoROI = []

    for i in CycleTwoYs:
        ROI = (i/4.39)*100
        ROINEW = int(ROI)
        CycleTwoROI.append(int(ROINEW))

    plt.text(312000,30000,"40000%")
    cycle1fig, = plt.plot(range(int(312000)),CycleTwoROI,label="Cycle 1",color=(0,0.8,0.8))    
    

def Cycle2():
    Close2015to2017 = data.loc[720000:2000000,["Close","Year"]]
    CycleThreeYs = Close2015to2017["Close"].tolist()
    
    CycleThreeROI = []

    for i in CycleThreeYs:
        ROI = (i/170)*100
        ROINEW = int(ROI)
        CycleThreeROI.append(int(ROINEW))

    plt.text(1180001,13000,"12000%")    
    plt.plot(range(int(1280001)),CycleThreeROI,label="Cycle 2",color=(0,0,1))
    
    
def Cycle3():
    Close2018to2021 = data.loc[2480000:6000020,["Close","Year"]]
    CycleFourYs = Close2018to2021["Close"].tolist()
   
    CycleFourROI = []

    for i in CycleFourYs:
        ROI = (i/3000)*100
        ROINEW = int(ROI)
        CycleFourROI.append(int(ROINEW),)
        
    plt.text(1153769,2300,"2000%")
    plt.plot(range(int(1133769)),CycleFourROI,label="Cycle 3",color=(1,0,1))

#Prompts the user for a target ROI for the current cycle and plots this level along with a label containing the price per bitcoin
def PriceTarget():
    Target = input("Type a ROI Target as percentage: ")
    Target = int(Target)
    Targetx = []
    for i in range(1500000):
        Targetx.append(i)
        
    Targety = []
    for i in range(1500000):
        Targety.append(Target)
        
    DollarTarget = (int(Target)*3000)/100
    DollarTarget = int(DollarTarget)
    DollarTarget = str(DollarTarget)
    
    plt.text(1300000,int(Target+80),"$" + DollarTarget + " or " + str(Target) + "%")
    fig, = plt.plot(Targetx,Targety,label=("$" + DollarTarget + " or " + str(Target) + "%"),linestyle="--")
    
    
    
    
def AddPriceTarget():
    Answer = input("Would you like to plot another price target?: ")
    Answer = str(Answer)
    if (Answer == "yes"):
        PriceTarget()
        AddPriceTarget()
    else:
        print("Later Space Cowboy")
    
    
    
Close2018to2021 = data.loc[2360000:3613768,["Close","Year"]]

#Sets the y axis to a logarithmic scale to better visualize trends

plt.yscale("log")
Cycle1()
Cycle2()
Cycle3()
ax.set_facecolor((0.87,0.87,0.87))
fig.set_facecolor((0.87,0.87,0.87))
plt.legend(loc="upper left")
plt.title("Bull Market ROI Comparison 2012-Present",loc="center")
plt.ylabel("ROI in Percent")
plt.pause(1)
PriceTarget()
plt.pause(1)
AddPriceTarget()
plt.show()








