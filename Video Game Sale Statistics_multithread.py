import threading
import pandas

Data_Table = pandas.read_csv('video-game-sales.csv')

def find_max():
    Max_Sale = Data_Table['Global_Sales'].max()
    print("max sale: " , Max_Sale)

def find_min():
    Min_Sale = Data_Table['Global_Sales'].min()
    print("min sale: " , Min_Sale)

def main():
    max_thread = threading.Thread(target= find_max)
    min_thread = threading.Thread(target= find_min)

    max_thread.start()
    min_thread.start()

    max_thread.join()
    min_thread.join()

if __name__ == "__main__":
    main()