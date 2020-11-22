""" this project is related to covid-19 information ,the api used in this application is taken from postman site
, The date of making this application in September 1, 2020 at 9.00 PM,
 made by Himanshu Sharma B.E 1St Year
No @CopyRight Content """

from tkinter import *  # all the Graphical User kits inside this module
import json
import requests   #this  module will request for the url (API) of covid19 status
from tkinter import colorchooser   #this module will change the color of background
from PIL import Image,ImageTk  #this will support png and jpg formate
import tkinter.messagebox as msg #pop up for the application
import time
import datetime
import webbrowser #for opening the sites
import matplotlib.pyplot as plt #for making the graph



"""all the function will define here """
def changeColor():#this will give the option to user for changing the backgroundColor
    colorTeller=colorchooser.askcolor()
    root.config(bg=f"{colorTeller[1]}")
    covidHeading.config(bg=f"{colorTeller[1]}")
    f1.config(bg=f'{colorTeller[1]}')
    f9.config(bg=f"{colorTeller[1]}")

def infoAdmin(): # give the information of admin i.e Himanshu the Great...
    admin=Toplevel()
    admin.title("Admin Information")
    admin.minsize(450,320)
    admin.maxsize(450,320)
    Label(admin,text="Admin Info",font="Elephant 16 bold underline",pady=7).pack(padx=5,pady=5)
    f2=Frame(admin,width=500,height=500,pady=10)
    f2.pack()
    adminPic=Image.open('admin.jpg')
    inserAdmin=ImageTk.PhotoImage(adminPic)
    picinsert4=Label(f2,image=inserAdmin)
    picinsert4.pack(padx=6,pady=6,side=LEFT)
    f3=Frame(f2,)
    f3.pack(side=LEFT)
    Label(f3,text="Himanshu Shamra\n B.E 1st Year\n9506891090\n",font="Arial 16 bold",padx=5,pady=5,bd=2,
          relief=SUNKEN,fg="green").pack(padx=5,side=TOP,anchor=N)
    Button(admin,text="Close",bg="red",fg="black",font="Elephant 12",command=admin.destroy).pack(fill=X)


    admin.mainloop()

def information():#information about the api and the post master
    info=Toplevel()
    info.title("Information..")
    info.maxsize(1000,550)
    info.iconbitmap('sui.ico')
    Label(info,text="Information",font="Elephant 16 underline",pady=8).pack(pady=6)
    F5=Frame(info)
    F5.pack()
    with open('information.txt') as printInformation:
        Label(F5,text=f'{printInformation.read()}',font="arial 16",pady=10,padx=10).pack(fill=BOTH,padx=10,pady=10)
        Button(F5,text="Got it",width=100,bd=2,relief=GROOVE,bg="gray",fg="white",command=info.destroy).pack(pady=5)
    info.mainloop()

def Register():#submit the user information


    def submit(name,mobile): #after clicking the sunbmit button
        if name=="" or mobile=="" or len(mobile)<10:
            msg.showerror("Incorrect Data","The data provided by you is incorrect. please Check your user-name and mobile number once once..")
        else:
            with open("registerFor.txt","a") as writeAll:
                writeAll.write(f"{datetime.datetime.now()}")
                writeAll.write(f"\nThe Name is : {name} \n Mobile number is {mobile}\n")

                writeAll.write("----------------------------------\n")
                l=msg.askyesno("info","Form Submitted Successfully \n Do you want to Submit Anothe Form..")
                if(l==TRUE):
                    reg.destroy()
                    Register()
                else:
                    reg.destroy()



    reg=Toplevel()
    reg.title('Registration Form..')
    reg.maxsize(300,300)
    UserName=StringVar()
    UserMobile=StringVar()
    Label(reg,text="REGISTRATION",font="Elephant 16 underline",pady=5).pack(pady=5,padx=5)
    f6=Frame(reg,pady=10,bd=3,relief=SUNKEN)
    f6.pack()
    Label(f6,text="Name : ",font="Arial 15 bold",pady=5,padx=5).pack(pady=5,padx=5,side=LEFT)
    username=Entry(f6,textvariable=UserName,font="Arial 15 bold",justify="center",)
    username.pack(side=LEFT,pady=5,padx=5)
    f7 = Frame(reg, pady=10, bd=3, relief=SUNKEN)
    f7.pack()
    Label(f7, text="MOB : ", font="Arial 15 bold", pady=5, padx=5).pack(pady=5, padx=5, side=LEFT)
    usermobile = Entry(f7, textvariable=UserMobile, font="Arial 15 bold", justify="center", )
    usermobile.pack(side=LEFT, pady=5, padx=5)
    f8 = Frame(reg, pady=10, bd=3, relief=SUNKEN)
    f8.pack()
    Button(f8,text="Submit",font="Arial 15",bg="green",fg="white",
           command=lambda: submit(UserName.get(),UserMobile.get()) ).pack(side=LEFT,padx=5,pady=5)
    Button(f8,text="Cancel",font="Arial 15",bg="red",fg="white",command=reg.destroy,)\
        .pack(side=LEFT,padx=5,pady=5)

    reg.mainloop()


def cureInformation(): #this will say the cure of corona virus

    def  gotit(): #this will close the cure information window..
        cure.destroy()
        pass

    def readMore():#this will take the user in web site of WHO
        try:
            site="https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public/myth-busters"
            webbrowser.open_new_tab(site)
        except Exception as Error:
            msg.showerror(f'Internet Connection","Your Internet Connection is off..please check your internet connection'
                          f'{Error}')

    cure=Toplevel()
    cure.title("Cure Of Corona Virus")
    Label(cure,text="Cure Of Corona Virus",font="chiller 25 bold underline",pady=5,fg="green").pack(pady=5,padx=5)
    f8=Frame(cure,padx=5,pady=5,bd=4,relief=GROOVE)
    f8.pack(padx=5,pady=5)
    with open("Cure.txt") as cures:
        Label(f8,text=f"{cures.read()}",font="Arial 15 bold",bg="red",fg="black").pack(padx=5,pady=5)

    f8 = Frame(cure, padx=5, pady=5)
    f8.pack(padx=5, pady=5)
    Button(f8,text="Got It",width=50,padx=5,pady=5,bg="green",fg="black",font="Arial 15 bold",command=gotit).pack(padx=5,pady=5)
    Button(f8,text="Read More",width=50,padx=5,pady=5,bg="blue",fg="white",font="Arial 15 bold",command=readMore).pack(padx=5,pady=5)
    cure.mainloop()



"""for the covid status of all region main coding"""

def GlobalInfo(): #global information

    def graphicalView(total,countries,Bycountries,dayOne):
        # print("we are moving")#making the graph for given data
        activity=["Total Active","One Day","Total Countries","By country"]
        slices=[int(total),int(countries),int(Bycountries),int(dayOne)]
        # print("moving")

        colors=['r','g','y','b']

        plt.pie(slices,labels=activity,colors=colors,startangle=90,
                shadow=TRUE,explode=(0,0,0.1,0),radius=1.2,autopct='%1.1f%%')

        plt.legend()

        plt.show()



    globalin=Tk()
    globalin.maxsize(500,500)
    globalin.title("Global Information")
    globalin.iconbitmap('sui.ico')



    """menu done here """
    try:
        sendServer=requests.get('https://api.covid19api.com/stats')

        final=sendServer.json()

        """making menu"""
        mainmenu1 = Menu(globalin)
        m6 = Menu(mainmenu1, tearoff=0)

        # mainmenu1.add_cascade(label="Graphical View",
        #                       menu=m6,
        #                       command=lambda:graphicalView(final['Total'],final['Countries'],final['ByCountry'],final['DayOne']))
        # mainmenu1.add_cascade(label="Exit", command=quit)
        # globalin.config(menu=mainmenu1)


        """making frame"""

        Label(globalin,text="Global Information",font="Arial 15 bold underline",bd=3,relief=SUNKEN).pack(pady=15)

        F10=Frame(globalin,padx=5,pady=15)
        F10.pack(padx=10,pady=20)

        Label(F10,text=f"Total Case \n \n{final['Total']}",font="Arial 13 bold underline",fg="red").pack(padx=5,pady=5,side=LEFT)
        Label(F10,text=f"Total Countries \n \n{final['Countries']}",font="Arial 13 bold underline",fg="green").pack(padx=5,pady=5,side=LEFT)
        Label(F10,text=f"By Countries \n \n{final['ByCountry']}",font="Arial 13 bold underline",fg="blue").pack(padx=5,pady=5,side=LEFT)

        F11 = Frame(globalin, padx=5, pady=15)
        F11.pack(padx=10, pady=20)

        Label(F11, text=f"In One Day \n \n{final['DayOne']}",font="Arial 13 bold underline",fg="red").pack(padx=5, pady=5, side=LEFT)
        Label(F11, text=f"Update \n \n{final['AllUpdated']}",font="Arial 13 bold underline",fg="green").pack(padx=5, pady=5, side=LEFT)

        try:
            globalin.destroy()
        except Exception as g:
            print(g)

    except EXCEPTION as err:
        pass
    globalin.mainloop()





def stateData():

    def graph(data):

        left=[]
        height=[]
        nameState=[]
        next=0

        for i in data:
             next += 1
             left.append(next)

        for i in data:

            height.append(i[1])

        for i in data:
            nameState.append(i[0][0:3])

        plt.bar(left,height,tick_label=nameState,width=0.9,color = ['red','green','blue','yellow'])

        plt.xlabel('State Name')
        plt.ylabel('Cases')

        plt.title("State information of covid ")

        plt.show()





    state=Toplevel()
    state.title("State information")
    state.iconbitmap('sui.ico')
    Label(state,text="Countries Information",font="Arial 18 bold underline",bd=1,relief=SUNKEN).pack(padx=10,pady=15)


    try:
        sendServer = requests.get('https://api.covidindiatracker.com/state_data.json')

        final = sendServer.json()

        datastore=[]

        f11=Frame(state,bd=3,relief=SUNKEN,bg="blue")
        f11.pack(padx=5,pady=10)


        for i in final:
            datastore.append([i['state'],i['confirmed'],i['active'],i['recovered'],i['deaths']])

        indexNumber=0

        lb = Listbox(f11,width=500,height=500,font="Arial 12 bold ",fg="green")
        lb.pack(padx=5, pady=10)



        for key in datastore:
            indexNumber += 1
            lb.insert(indexNumber,f'{key[0]}  Total : {key[1]} -  Active : {key[2]} -  Recovered : {key[3]} -  Deaths : {key[4]}')

        graph(datastore)





    except:
        msg.showerror("Network Error","Please check your Internet Connection....")




    state.mainloop()


def country():
    def graphcountry(data):


        deth=[]
        for i in data:
            deth.append(i[4])

        range=(0,max(deth))

        bins=12

        plt.hist(deth
                 ,bins,range,color="green",histtype="stepfilled",rwidth=0.8)

        plt.ylabel('Top Countries')
        plt.xlabel('No. of death')

        plt.title("Countries info")
        plt.show()






    country=Toplevel()
    country.title("Country information")
    country.iconbitmap('sui.ico')
    Label(country,text="Countries  Information Covid 19" ,font="Arial 18 bold underline",bd=1,relief=SUNKEN).pack(padx=10,pady=15)


    try:
        sendServer = requests.get('https://api.covid19api.com/summary')

        final = sendServer.json()

        datastore=[]

        f11=Frame(country,bd=3,relief=SUNKEN,bg="blue")
        f11.pack(padx=5,pady=10)


        for i in final['Countries']:
            datastore.append([i['Country'],i['TotalConfirmed'],i['NewConfirmed'],i['TotalRecovered'],i['TotalDeaths']])

        indexNumber=0

        lb = Listbox(f11,width=500,height=500,font="Arial 12 bold ",fg="red")
        lb.pack(padx=5, pady=10)



        for key in datastore:
            indexNumber += 1
            lb.insert(indexNumber,f'{key[0]}  Total : {key[1]} -  New Confirm : {key[2]} -  Recovered : {key[3]} -  Deaths : {key[4]}')

        graphcountry(datastore)





    except:
        msg.showerror("Network Error","Please check your Internet Connection....")




    country.mainloop()


def district():
    def graphicaldis(total):

        # print("we are moving")#making the graph for given data
        activity=[]
        slices=[]
        newtouple=[]
        number=0
        for i in total:
            activity.append(i[0])
            slices.append(i[1])

            newtouple.append(number)

        # slices=[int(total),int(countries),int(Bycountries),int(dayOne)]
        # print("moving")


        colors=['r','g','y','b']

        plt.pie(slices,labels=activity,colors=colors,startangle=90,
                shadow=TRUE,explode=tuple(newtouple),radius=1.5,autopct='%1.1f%%')

        plt.legend()

        plt.show()


    dis=Toplevel()
    dis.title("District information")
    dis.iconbitmap('sui.ico')
    Label(dis,text="District Information Covid 19" ,font="Arial 18 bold underline",bd=1,relief=SUNKEN).pack(padx=10,pady=15)



    sendServer = requests.get('https://api.covidindiatracker.com/state_data.json')

    final = sendServer.json()

    datastore=[]

    for i in final:
            if(i["state"]=="Uttar Pradesh"):
                for k in i["districtData"]:
                    datastore.append([k['id'],k['confirmed'],k["id"],k['recovered'],k["deaths"]])

    f11 = Frame(dis, bd=3, relief=SUNKEN, bg="blue")
    f11.pack(padx=5, pady=10)
    lb = Listbox(f11, width=500, height=500, font="Arial 12 bold ", fg="blue")
    lb.pack(padx=5, pady=10)
    indexNumber = 0

    for key in datastore:
        indexNumber += 1
        lb.insert(indexNumber,
                  f'{key[0]}  Total : {key[1]} -  Name: {key[2]} -  Recovered : {key[3]} -  Deaths : {key[4]}')

    graphicaldis(datastore)






    dis.mainloop()




# making the gui window here
root=Tk()
root.title("Covid 19 Tracker")
root.iconbitmap('sui.ico')
root.geometry('1000x660')

"""making the menubar.."""

mainMenu=Menu(root)

m1=Menu(mainMenu,tearoff=0)
m1.add_command(label="Change Color",command=changeColor)
m1.add_command(label="Info",command=information)
m1.add_command(
    label="Admin",command=infoAdmin
)

m2=Menu(mainMenu,tearoff=0)
m2.add_command(label="Register",command=Register)

m3=Menu(mainMenu,tearoff=0)
m3.add_command(label="Cure information",command=cureInformation)

mainMenu.add_cascade(label="File",menu=m1)
mainMenu.add_cascade(label="Register",menu=m2)
mainMenu.add_cascade(label="Cure info",menu=m3)
mainMenu.add_cascade(label="Exit",command=exit)
root.config(menu=mainMenu)

"""menu work finish here"""

"""making a label for the covid 19 heading in label"""

covidHeading=Label(root,text="Covid-19 Status (Tracker) ", font="Elephant 27  underline",padx=20)
covidHeading.pack(padx=15,pady=10,side=TOP)

"""Inserting Image """

picCovid=Image.open('covid1.jpg')
picinsert=ImageTk.PhotoImage(picCovid)

picCovid1=Image.open('covid3.jpg')
picinsert2=ImageTk.PhotoImage(picCovid1)

f1=Frame(root,bd=4,relief=SUNKEN)
f1.pack(pady=30)
piclabel=Label(f1,image=picinsert)
piclabel.pack(side=LEFT,padx=20,pady=20)

piclabel1=Label(f1,image=picinsert2)
piclabel1.pack(side=LEFT,padx=20,pady=20)

picCovid3=Image.open('images.jpg')
picinsert3=ImageTk.PhotoImage(picCovid3)

piclabel3=Label(f1,image=picinsert3)
piclabel3.pack(side=LEFT,padx=20,pady=20)

"""Making the button for the user option"""
f9=Frame(root,bd=4,relief=GROOVE,padx=5,pady=5)
f9.pack(padx=5,pady=25)

Button(f9,text="Global Data",bd=2,relief=GROOVE,font="Arial 18 bold",pady=5,command=GlobalInfo).pack(padx=5,pady=15,side=LEFT)
Button(f9,text="Country Data",bd=2,relief=GROOVE,font="Arial 18 bold",pady=5,command=country).pack(padx=5,pady=15,side=LEFT)
Button(f9,text="State Data",bd=2,relief=GROOVE,font="Arial 18 bold",pady=5,command=stateData).pack(padx=5,pady=15,side=LEFT)
Button(f9,text="District Data(U.P)",bd=2,relief=GROOVE,font="Arial 18 bold",pady=5,command=district).pack(padx=5,pady=15,side=LEFT)


"""making taskbar"""

taskBar=Frame(root,relief=GROOVE,bd=3)
taskBar.pack(side=BOTTOM,anchor="s",fill=X)

ltime=Label(taskBar,text=f"{time.asctime(time.localtime(time.time()))}",)
ltime.pack(side=LEFT,padx=10)

ltime=Label(taskBar,text=f"Postman Api (Covid-19 Update) `Himanshu Sharma",)
ltime.pack(side=RIGHT,padx=10)

root.mainloop()



"""finsh this project in september 2 ,2020 at 5.27 A.M"""




