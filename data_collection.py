import pandas as pd
import matplotlib.pyplot as plt
import csv
import datetime
import time
from main import GetBatteryLevel

head = ["Sr_No." , "Battery_level","Time","Date"]
data = [[1,10],[2,12],[3,13]]

# open csv file in append mode
with open("./PYTHON/Macbook_battery_data/Data.csv","w+") as file:
    write = csv.writer(file)
    read = csv.reader(file)
    write.writerow(head)

    for i in range(10):
        data = [i+1,GetBatteryLevel(),str(datetime.datetime.now()).split(" ")[1],datetime.date.today()]
        write.writerow(data)
        time.sleep(2)

# convert current percentage in csv format

