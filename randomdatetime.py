import random
import time

def GetRandomDate(stardate, enddate):
    print("Printing random date between ", stardate, "and", enddate)
    randomgenerator=random.random()
    dateformat='%M/%d/%Y'
    starttime=time.mktime(time.strptime(stardate,dateformat))
    endtime=time.mktime(time.strptime(enddate , dateformat))
    randomtime=starttime + randomgenerator * (endtime - starttime)
    randomdate=time.strftime(dateformat, time.localtime(randomtime))
    return randomdate

print("Random date is: " , GetRandomDate("1/1/2020","12/12/24"))
