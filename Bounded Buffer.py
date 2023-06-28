##########################################################
# LIBRARIES
##########################################################

import threading
import random
import time
from collections import deque

##########################################################
# GLOBAL VARIABLES
##########################################################

# define buffer size 10
Buffer_Size = 10
Buffer      = deque(maxlen= Buffer_Size)

# buffer outputs & inputs counter 
In_C  = 0   
Out_C = 0

##########################################################
# PRODUSER FUNCTION
##########################################################

def producer() :
    # produce next item
    while(True) :
        global In_C , Out_C
        while( ((In_C + 1) % Buffer_Size) == Out_C) :
            print("*** Producer: Buffer is Full. Please wait...")
            time.sleep(random.random())
            continue
        Buffer.append(random.randint(1,9))
        In_C = (In_C + 1) % Buffer_Size
        print(Buffer)

##########################################################
# CONSUMER FUNCTION
##########################################################

def consumer() :
    # next item consume
    while(True) :
        global In_C , Out_C
        while(In_C == Out_C) :
            print("+++ Consumer: Buffer is Empty. Please wait...")
            time.sleep(random.random())
            continue
        Buffer.pop()
        Out_C = (Out_C + 1) % Buffer_Size
        print(Buffer)

##########################################################
# MAIN FUNCTION
##########################################################

def main() :
    # creat Threads
    producer_T = threading.Thread(target= producer)
    consumer_T = threading.Thread(target= consumer)

    producer_T.start()
    consumer_T.start()
    
    producer_T.join()
    consumer_T.join()

##########################################################
# CALL MAIN
##########################################################

if __name__ == "__main__" :
    main()
