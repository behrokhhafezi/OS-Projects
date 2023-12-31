##########################################################
# LIBRARIES
##########################################################

import threading
import pandas
import time

##########################################################
# GLOBAL VARIABLES
##########################################################

Data_Table = pandas.read_csv('video-game-sales.csv')

##########################################################
# FIND MAX FUNCTION
##########################################################

def find_max():
    Max_Sale = Data_Table['Global_Sales'].max()
    print("max sale: " , Max_Sale)

##########################################################
# FIND MIN FUNCTION
##########################################################

def find_min():
    Min_Sale = Data_Table['Global_Sales'].min()
    print("min sale: " , Min_Sale)

##########################################################
# MAIN FUNCTION
##########################################################

def main():
    Start_Time = time.time()

    max_thread = threading.Thread(target= find_max)
    min_thread = threading.Thread(target= find_min)

    max_thread.start()
    min_thread.start()

    max_thread.join()
    min_thread.join()

    End_Time = time.time()
    # Calculate the total execution time of the program
    Total_Time = End_Time - Start_Time
    print("Total spend time: " , Total_Time)

##########################################################
# USE MAIN FUNCTION
##########################################################

if __name__ == "__main__":
    main()
