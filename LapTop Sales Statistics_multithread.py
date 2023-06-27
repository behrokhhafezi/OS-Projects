##########################################################
# LIBRARIES
##########################################################

import time
import threading
import requests
import pandas as pd
from bs4 import BeautifulSoup

##########################################################
# GLOBAL VARIEBLES
##########################################################

Start_Time = time.time()

# saving the site url
url    = 'https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA_%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE~Category~40'

# check the url site to make sure that we can use their data
pages  = requests.get(url)

# parse sites program
soup   = BeautifulSoup(pages.text , "lxml")

# finding all of price box addresses
Prices = soup.find_all("div" , class_ = "price-box")

# convert price box addresses to their contents
Price_List = []
for i in Prices:
    Price = i.text
    Price_List.append(Price)
#print(price_list)

# finding all of name box addresses
Names = soup.find_all("h2" , class_ = "item-title")

# convertbox box addresses to their contents
Name_List = []
for i in Names:
    Name = i.text
    Name_List.append(Name)
#print(name_list)

##########################################################
# FIND MAX FUNCTION
##########################################################

def find_max():
    # find maximum price 
    Max_Price     = max(Price_List)
    Max_Indx      = Price_List.index(Max_Price)
    Max_Item_Name = Name_List[Max_Indx]
    print( "* The most expensive laptop is '", Max_Item_Name , "' with a price of ' ", Max_Price , " '.\n")

##########################################################
# FIND MIN FUNCTION
##########################################################

def find_min():
    # find minimum price item 
    Min_Price     = min(Price_List)
    Min_Indx      = Price_List.index(Min_Price)
    Min_Item_Name = Name_List[Min_Indx]
    print( "* The cheapest laptop is '", Min_Item_Name , "' with a price of ' ", Min_Price , " '.")

##########################################################
# MAIN FUNCTION
##########################################################

def main():

    find_max_thread = threading.Thread(target= find_max)
    find_min_thread = threading.Thread(target= find_min)

    find_max_thread.start()
    find_min_thread.start()

    find_max_thread.join()
    find_min_thread.join()

    End_Time   = time.time()
    Total_Time = End_Time - Start_Time
    print("total spending time: " , Total_Time)

##########################################################
# USE MAIN FUNCTION
##########################################################

if __name__ == "__main__":
    main()
