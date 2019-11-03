import  ast
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys

file = open("CityDict.txt",'r')
line = file.read()
CityDict = ast.literal_eval(line)

driver = webdriver.Chrome("C://Users//bisha//Documents//chromedriver_win32//chromedriver.exe")
driver.get("https://us.megabus.com/journey-planner/map")

From = driver.find_element_by_id("startingAt")
GoingTo= driver.find_element_by_id("goingTo")




file = open("AdjList1", "w")

UnvisitedNodes = True
VisitedNodes =[]

while UnvisitedNodes == True:

    From.send_keys()
    From.send_keys(Keys.DOWN)
    From.send_keys(Keys.TAB)
    oriCity = From.get_attribute("value")
    GoingTo.send_keys()

    if (oriCity not in VisitedNodes):
        VisitedNodes.append(oriCity)
    else:
        break

    repeat = True
    List = [CityDict[oriCity],[]]


    while (repeat == True):
        GoingTo.send_keys(Keys.DOWN)
        destCity = GoingTo.get_attribute("value")


        if destCity:

            if (CityDict[destCity] not in List[1]):


                if (CityDict[destCity] != List[0]):
                    List[1].append(CityDict[destCity])
                    #print(oriCity+" TO "+destCity)

            else:

                break

    print(List)
    file.write(List.__str__())
    file.write('\n')
file.close()



'''addfile = open("AdjList",'r')
for line in addfile.readlines():
    citylist =[0,[]]
    numlist = ast.literal_eval(line)
    citylist[0]=list(CityDict.keys())[list(CityDict.values()).index(numlist[0])]
    for item in numlist[1]:
        city = list(CityDict.keys())[list(CityDict.values()).index(item)]
        citylist[1].append(city)
    print(citylist)'''