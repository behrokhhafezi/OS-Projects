##########################################################
# LIBRARIES
##########################################################

import threading
import random
import time

##########################################################
# PHILOSOPHER CLASS
##########################################################

# inheriting threading class in Thread module
class Philosopher(threading.Thread):
    # check that everyone is finished eating
    running = True  

    def __init__(self, index, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.index       = index
        self.forkOnLeft  = forkOnLeft
        self.forkOnRight = forkOnRight

    def run(self):
        while(self.running):
            # Philosopher is thinking
            time.sleep(random.random())
            print ('Philosopher %s is hungry.' % self.index)
            self.dine()

    def dine(self):
        # if both forks are free then philosopher can eat
        fork1 , fork2 = self.forkOnLeft , self.forkOnRight
        while (self.running):
            # wait for left fork
            fork1.acquire() 
            locked = fork2.acquire(False)
            # if right fork is not available leave left fork 
            if (locked):
                break 
            fork1.release()
            print ('Philosopher %s swaps forks.' % self.index)
            fork1 , fork2 = fork2 , fork1
        else:
            return
        self.dining()
        #release both fork after dining
        fork2.release()
        fork1.release()
 
    def dining(self):			
        print ('Philosopher %s starts eating. '% self.index)
        time.sleep(random.random())
        print ('Philosopher %s finishes eating and leaves to think.' % self.index)

##########################################################
# MAIN FUNCTION
##########################################################

def main():
    # initialising array of forks
    forks = [threading.Semaphore() for n in range(5)] 

    # here (i+1)%5 is used to get right and left forks circularly between 1-5
    philosophers= [Philosopher(i, forks[i%5], forks[(i+1)%5])
            for i in range(5)]

    
    for p in philosophers:
        p.start()

    for p in philosophers:
        p.join()

##########################################################
# USE MAIN FUNCTION
##########################################################

if __name__ == "__main__":
    main()
