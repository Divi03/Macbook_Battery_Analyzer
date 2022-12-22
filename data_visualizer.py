import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/Applications/Files/PYTHON/Macbook_battery_data/Data.csv",usecols=['Sr_No.','Battery_level'])
df = pd.DataFrame(data)

# print(df['Battery_level'])
# c = ['red', 'yellow', 'black', 'blue', 'orange']

profit_color = [{p<30: 'red', 30<=p<=50: 'orange', p>50: 'green'}[True] for p in list(df['Battery_level'])]
plt.bar(df['Battery_level'],df['Sr_No.'],color=profit_color)
plt.show()