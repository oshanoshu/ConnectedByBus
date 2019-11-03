from bs4 import BeautifulSoup
import pdb
import re

class Results:
    def __init__(self,soupTag,startID,destID):
        self.StartID=startID
        self.DestID=destID
        self.StartingTime =""
        self.EndingTime=""
        self.Duration=""
        self.Price =""
        self.StartingAddress =""
        self.DestAddress=""
        self.Stops=[]
        self.extractResults(soupTag)

    def extractResults(self, soupTag):
        time = soupTag.find_all('span', attrs={'class': 'ticket__time__item'})
        duration = soupTag.find_all('span', attrs={'class': 'ticket__summary__text'})
        price = soupTag.find_all('span',attrs={'class':'ticket__price__item'})
        #stops = soupTag.find_all('span',attrs={'class':'ticket__stops__item'})
        busStops = soupTag.find_all('a',attrs={'data-gtm-id':"bus-stops-info"})


        self.StartingTime=str(time[0].contents[0]) + str(time[0].contents[1].string)
        self.EndingTime =str(time[1].contents[0]) + str(time[0].contents[1].string)
        self.Duration = (duration[0].string).split(',')[0]
        if not str(self.Duration).__contains__("m"):
            self.Duration = self.Duration +" 00m"
        self.Price = float((str(price[0].string)).replace("$",""))
        self.StartingAddress=busStops[0]['data-gtm-label']
        self.DestAddress=busStops[-1]['data-gtm-label']
        if(len(busStops) >2 ):
            for i in range(1,len(busStops)-1):
                self.Stops.append(busStops[i]['data-gtm-label'])

    def ReturnKey(self):
        print(re.sub("\D", "", self.Duration))
        return  re.sub("\D", "", self.Duration)