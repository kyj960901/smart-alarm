import math

def calculate_distance(txPower, rssi):
    if rssi==0:
        return -1 #error
    
    ratio = rssi/txPower
    print(ratio)
    if ratio<1:
        return ratio**10
    
    else:
        accuracy = 0.89976*(ratio**7.7095)+0.111
        return accruacy


print(calculate_distance(-65, -59))