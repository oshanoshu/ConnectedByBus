
from flask import Flask, render_template, redirect, request, url_for
from message import Twilios
import pdb
import SearchResults
import FindPathFin
from StartingPoint import cheapRoute
import ast 
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    
    if request.method=="POST":
        global plist
        plist=[]
        print(request)
        global origin
        origin= request.form['from']
        plist.append(origin)
        global destination 
        destination= request.form['destination']
        plist.append(destination)
        global  date
        date= request.form['date']
        plist.append(date)


        file=open("CityDict.txt")
        for line in file.readlines():
            dicts=ast.literal_eval(line)
        org=dicts[origin]
        print(org)
        dest=dicts[destination]
        print(dest)
        cheaproute=cheapRoute(str(org),str(dest),date)
        cheap=[]
        cheap.append(origin)
        print(cheap[0])
        cheap.append(destination)
        print(cheap[1])
        #starttime=cheaproute[0][0].StartingTime
        #endtime=cheaproute[0][0].EndingTime
        # mytime= starttime+" "+ endtime
        # cheap.append(mytime)
        # print(cheap[2])


        cheap.append(cheaproute[0][0].Duration)
        print(cheap[3])
        cheap.append(cheaproute[0][0].Stops)
        print(cheap[4])
        cheap.append(cheaproute[0][0].Price)
        print(cheap[5])
        cheap.append(cheaproute[0][0].StartingAddress)
        print(cheap[6])
        cheap.append(cheaproute[0][0].DestAddress)
        print(cheap[7])
        return render_template("details.html",data=cheap)
    else:
        return render_template("home.html")

@app.route("/details")
def details():
    # if request.method=="POST":
    #     email=request.form['email']
    #     phone=request.form['phone']
    #     yesEmail=request.form['emailMe']
    #     if(yesEmail=="yesEmail"):
    #         email(email)
    #     yesText=request.form['textMe']
    #     if yesText=="yesText":
    #         twili=Twilios()
    #         twili.message(phone,"What's up?")

    return render_template("details.html")

if __name__ == "__main__":  
    app.run(debug=True)
