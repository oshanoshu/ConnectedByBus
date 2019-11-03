from selenium import webdriver
from bs4 import BeautifulSoup
from Result import Results

ResultArray = []

def Launchwindow(start=123,end=100,date='2019-11-03'):
    driver = webdriver.Safari()
    url ="https://us.megabus.com/journey-planner/journeys?days=1&concessionCount=0&departureDate={}&destinationId={}&inboundDepartureDate=2019-10-31&inboundOtherDisabilityCount=0&inboundPcaCount=0&inboundWheelchairSeated=0&nusCount=0&originId={}&otherDisabilityCount=0&pcaCount=0&totalPassengers=1&wheelchairSeated=0".format(date,end,start)

    driver.get(url)
    soup=""
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")


    #result = soup.find_all('div', attrs={
      #  'class': 'panel-group ng-tns-c9-1 ng-trigger ng-trigger-loadingState ng-star-inserted'})
    return soup



def find_elem(tag):
        return tag.has_attr('data-index')

def PrintResult(soup,startID,destID):

    ResultArray=[]
    ResultArray.clear()
    divResult = soup.find_all(find_elem)

    for item in divResult:
        ResultArray.append(Results(item,startID,destID))


    return ResultArray
    '''for objects in ResultArray:
        print(objects.StartingTime + " " + objects.EndingTime)
        print(objects.Duration)
        print(objects.StartingAddress)
        print(objects.DestAddress)
        print(objects.Price)
        print(objects.Stops)
        print("----------------------")
'''
#result=Launchwindow()
#PrintResult(result)
