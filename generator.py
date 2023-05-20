import requests
import random
import argparse

URL = "http://192.168.4.1"
DEFAULT_SSIDS = 50

def getControlNum(pesel):
    controlShit = [1,3,7,9,1,3,7,9,1,3]
    Sum = 0
    for c in range(0,10):
       Sum += (int(pesel[c]) * controlShit[c]) % 10
    Sum %= 10
    return str(10 - Sum)

def getPesel():
    year = str(random.choice([random.randint(60, 99), random.randint(0,11)]))
    month = str(random.randint(1,12))
    day = str(random.randint(1,30))
    rand = str(random.randint(0,9999))
    
    
    if len(year) == 1:
        year = "0" + year
    if len(rand) == 1:
        rand = "000" + rand
    if len(rand) == 2:
        rand = "00" + rand
    if len(rand) == 3:
        rand = "0" + rand
    if len(day) == 1:
        day = "0" + day
    if int(year) < 60:
        month = str(int(month) + 20)        
    if len(month) == 1:
        month = "0" + month
    
    pesel = year + month + day + rand
    pesel += getControlNum(pesel)
    return pesel
    
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--ssids", type=int)
    
    args = parser.parse_args()
    ssids = args.ssids
    if ssids == None:
        ssids = DEFAULT_SSIDS
    
    for x in range(0, ssids):
        print(requests.get(URL + "/run?cmd=add ssid \"Pfizer Chip ID " + getPesel()+"\" -f -cl 1 -wpa"))

