##########################################################
# LIBRARIES
##########################################################

import pandas

##########################################################
# MAIN
##########################################################

# reading 'video-game-sales.csv' file and make a table out of it
Data_Table = pandas.read_csv('video-game-sales.csv')

# find maximum global sale in video games
Max_Sale = Data_Table['Global_Sales'].max()

# find maximum global sale in video games
Min_Sale = Data_Table['Global_Sales'].min()

print("max sale: " , Max_Sale)
print("min sale: " , Min_Sale)
