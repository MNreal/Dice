import numpy as np;
import random as rd;
import time;

a = input("Do you want to roll the dice?");

if (a == "y" or a =="Y" or a == "Yes" or a == "yes"):
    print ("rolling dice...");

    time.sleep(3);

    print ("Loading number");

    time.sleep(2);

    print (np.random.randint(1, 6));

else:
    print ("exit");

