import pandas

Data_Table = pandas.read_csv('video-game-sales.csv')

Max_Sale = Data_Table['Global_Sales'].max()

Min_Sale = Data_Table['Global_Sales'].min()

print("max sale: " , Max_Sale)
print("min sale: " , Min_Sale)