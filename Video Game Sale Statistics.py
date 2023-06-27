##########################################################
# LIBRARIES
##########################################################

import pandas
import time

##########################################################
# MAIN
##########################################################

Data_Table = pandas.read_csv('video-game-sales.csv')

Start_Time = time.time()

Max_Sale = Data_Table['Global_Sales'].max()

Min_Sale = Data_Table['Global_Sales'].min()

End_Time   = time.time()
Total_Time = End_Time - Start_Time

print("max sale: " , Max_Sale)
print("min sale: " , Min_Sale)
print("Total spending time: " , Total_Time)
