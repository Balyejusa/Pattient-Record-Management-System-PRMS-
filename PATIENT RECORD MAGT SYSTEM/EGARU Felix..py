from tkinter import *
import tkinter as tk 
from tkinter import ttk
import sqlite3
import tkinter.messagebox
from tkinter import scrolledtext
conn=sqlite3.connect("wak.db")
c=conn.cursor()

def main(frame):
    frame.tkraise()

window=Tk()
window.geometry("2200x740")

frame1=Frame(window,width=2200,height=740,bg="white")
frame1.grid(row=0,column=0,sticky="news")

frame2=Frame(frame1,width=2000,height=80,bg="maroon")
frame2.place(x=0,y=0)

imagehome = PhotoImage(file="waks.png")
w = imagehome.width()
h = imagehome.height()
window.geometry("%dx%d+0+0" % (w, h))
panel1 =Label(frame1, image=imagehome)
panel1.place(x=-180,y=80)

panel1.image = imagehome

label1 = Label(frame1,text = "Password:" ,bg = "white", fg="blue", font = "Times 18 bold")
label1.place(x=294,y=350)
label2 = Label(frame1,text = "User ID:" ,bg = "white", fg="blue", font = "Times 18 bold")
label2.place(x=310,y=280)

okbaton=PhotoImage(file="max.png")
baton=Label(frame1,image=okbaton,height=210)
baton.place(x=400,y=80)

label3=Label(frame2,text = " Welcome To The PATIENT RECORD MANAGEMENT SYSTEM (PRMS)" ,bg = "maroon", fg = "white", font = "Times 22 bold",)
label3.place(x=21,y=20)


entry1=Entry(frame1,width=20,bg="white",fg="black",font="Times 18",relief="ridge",bd=4)
entry1.place(x=420,y=277)

entry2=Entry(frame1,width=17,bg="white",fg="black", font="Courier 18",show="*",relief="ridge",bd=4)
entry2.place(x=420,y=347)

def reply():
    userid=entry1.get()
    paswad=entry2.get()
    lista=[]
    lista2=[]
    lista3=[]
    lista4=[]
    sql="SELECT * FROM details"
    c.execute(sql)
    rows=c.fetchall()
    for row in rows:
        lista.append(row[0])
        lista2.append(row[3])
    print(lista)
    print(lista2)
    for i in lista:
        try:
            if i.startswith("A"):
                w=i[:100]
                lista3.append(w)
        except AttributeError:
##            lab=Label(window,bg="white",text="Please always create your Admin userid beginning with an A as well \nas User account id begginng with a C ",fg="red",font="Times 13")
##            lab.place(x=300,y=500)
            print("Please always create your Admin passwords beginning \nwith an A")
    print(lista3)
    for x in lista:
        try:
            if x.startswith("C"):
                v=x[:100]
                lista4.append(v)
        except AttributeError:
            print("Please always create your User passwords beginning \nwith an C")
            
    print(lista4)

    entry1.delete(0,END)
    entry2.delete(0,END)
    
    if userid in lista3 and paswad in lista2:
        print("Welcome")
        def maxin(frame):
            frame.tkraise()

            
        pagesix=Frame(window,width=2000,height=700,bg="white")
        pageseven=Frame(window,width=2000,height=700,bg="white")
        pagemor=Frame(window,width=2000,height=700,bg="white")
        create_frame=Frame(window,width=2000,height=700,bg="white")
        
        for frame in (create_frame,pagesix,pageseven,pagemor):
            frame.grid(row=0,column=0,sticky="news")

        image1 = PhotoImage(file="waks.png")
        w = image1.width()
        h = image1.height()
        window.geometry("%dx%d+0+0" % (w, h))
        panel1 =Label(create_frame, image=image1)
        panel1.place(x=0,y=120)

        panel1.image = image1

        image2 = PhotoImage(file="waks.png")
        w = image2.width()
        h = image2.height()
        window.geometry("%dx%d+0+0" % (w, h))
        panel2 =Label(pagesix, image=image2)
        panel2.place(x=0,y=120)

        panel2.image = image2

        image3 = PhotoImage(file="waks.png")
        w = image3.width()
        h = image3.height()
        window.geometry("%dx%d+0+0" % (w, h))
        panel3 =Label(pageseven, image=image3)
        panel3.place(x=0,y=120)

        panel3.image = image3

        image4 = PhotoImage(file="waks.png")
        w = image4.width()
        h = image4.height()
        window.geometry("%dx%d+0+0" % (w, h))
        panel4 =Label(pagemor, image=image4)
        panel4.place(x=0,y=120)

        panel4.image = image4
            
        frame2=Frame(create_frame,bg="maroon",width=1900,height=80)
        frame2.place(x=0,y=0)
            
        baton1=Button(frame2,text="Create Accounts",font="Times 17 bold",relief="raised",bg="white",fg="red",width=16)
        baton1.place(x=70,y=35)

        baton1=Button(frame2,text="Staff",font="Times 17 bold",relief="raised",bg="white",fg="green",width=16,command=lambda:maxin(pagesix))
        baton1.place(x=287,y=35)
        baton1=Button(frame2,text="View records",font="Times 17 bold",relief="raised",bg="white",fg="green",width=16,command=lambda:maxin(pageseven))
        baton1.place(x=504,y=35)
        baton1=Button(frame2,text="Mortury",font="Times 17 bold",relief="raised",bg="white",fg="green",width=16,command=lambda:maxin(pagemor))
        baton1.place(x=721,y=35)
            
        #Admin account
        label1=Label(create_frame,text="Administrator Account",font="Times 20",bg="white",fg="blue")
        label1.place(x=410,y=80)
        label2=Label(create_frame,text="Admin ID",font="Times 16",bg="white",fg="blue")
        label2.place(x=180,y=160)
        label3=Label(create_frame,text="Firstname",font="Times 16",bg="white",fg="blue")
        label3.place(x=180,y=220)
        label4=Label(create_frame,text="Lastname",font="Times 16",bg="white",fg="blue")
        label4.place(x=540,y=160)
        label5=Label(create_frame,text="Password",font="Times 16",bg="white",fg="blue")
        label5.place(x=540,y=220)

        tce10=StringVar()
        tce20=StringVar()
        tce30=StringVar()
        tce40=StringVar()
        
        entral176=Entry(create_frame,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tce10)
        entral176.place(x=280,y=160)
        entral276=Entry(create_frame,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tce20)
        entral276.place(x=280,y=220)
        entral376=Entry(create_frame,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tce30)
        entral376.place(x=640,y=160)
        entral476=Entry(create_frame,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tce40)
        entral476.place(x=640,y=220)
        
        def reply1():
            idy=tce10.get()
            fnm=tce20.get()
            lnm=tce30.get()
            paswd=tce40.get()
            if idy[0]=="A":
                sqli="INSERT INTO details(ID,fname,lname,password) VALUES(?,?,?,?)"
                c.execute(sqli,(idy,fnm,lnm,paswd))
                conn.commit()
                entral176.delete(0,END)
                entral276.delete(0,END)
                entral376.delete(0,END)
                entral476.delete(0,END)
                
                
                tkinter.messagebox.showinfo("Success","A new Admin account has been created")
            else:
                print("Begin your id with an uppercase A")
                lavd=Label(create_frame,text="Please create all your admin accounts begginning with \nan uppercase  'A'  followed by any characters ",fg="red",bg="white",font="Times 13")
                lavd.place(x=390,y=280)
            
        xx=Button(create_frame,text="Add Account",font="Times 14 bold",bg="white",fg="maroon",command=reply1)
        xx.place(x=800,y=280)

        ##User accounts
        label1=Label(create_frame,text="User Account",font="Times 20",bg="white",fg="blue",width=68)
        label1.place(x=0,y=350)
        label2=Label(create_frame,text="User ID",font="Times 16",bg="white",fg="blue")
        label2.place(x=180,y=450)
        label3=Label(create_frame,text="Firsname",font="Times 16",bg="white",fg="blue")
        label3.place(x=180,y=515)
        label4=Label(create_frame,text="Lastname",font="Times 16",bg="white",fg="blue")
        label4.place(x=540,y=450)
        label5=Label(create_frame,text="Password",font="Times 16",bg="white",fg="blue")
        label5.place(x=540,y=515)

        tvta19=StringVar()
        tvta20=StringVar()
        tvta21=StringVar()
        tvta22=StringVar()
        
        
        entr100=Entry(create_frame,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tvta19)
        entr100.place(x=280,y=450)
        entr200=Entry(create_frame,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tvta20)
        entr200.place(x=280,y=515)
        entr300=Entry(create_frame,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tvta21)
        entr300.place(x=640,y=450)
        entr400=Entry(create_frame,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tvta22)
        entr400.place(x=640,y=515)
        
       

        def reply2():
            idi=tvta19.get()
            fmn=tvta20.get()
            lmn=tvta21.get()
            pasd=tvta22.get()
            if idi[0]=="C":
                sqli="INSERT INTO details(ID,fname,lname,password) VALUES(?,?,?,?)"
                c.execute(sqli,(idi,fmn,lmn,pasd))
                conn.commit()
                entr100.delete(0,END)
                entr200.delete(0,END)
                entr300.delete(0,END)
                entr400.delete(0,END)
                
                
                tkinter.messagebox.showinfo("Success","A new User account has been created")
            else:
                print("Begin your id with an uppercase A")
                lavd=Label(create_frame,text="Please create all your user accounts begginning with \nan uppercase  'C'  followed by any characters of your choice",fg="red",bg="white",font="Times 13")
                lavd.place(x=390,y=600)

        xx=Button(create_frame,text="Add Account",font="Times 14 bold",bg="white",fg="maroon",command=reply2)
        xx.place(x=800,y=575)
        
        xx=Button(create_frame,width=8,text="Log Out",font="Times 12 bold",bg="white",fg="blue",command=lambda:main(frame1))
        xx.place(x=900,y=660)


        ##Staff
  
        frame2=Frame(pagesix,width=2000,height=80,bg="maroon")
        frame2.place(x=0,y=0)
        
        baton=Button(pagesix,text="Create Accounts",bg="white",fg="green",font="Times 17 bold",width=16,command=lambda:maxin(create_frame))
        baton.place(x=70,y=35)
        baton2=Button(pagesix,text="Staff",width=16,bg="white",fg="red",font="Times 17 bold")
        baton2.place(x=287,y=35)
        baton3=Button(pagesix,text="View Records",width=16,bg="white",fg="green",font="Times 17 bold",command=lambda:maxin(pageseven))
        baton3.place(x=504,y=35)
        baton4=Button(pagesix,text="Mortury",width=16,bg="white",fg="green",font="Times 17 bold",command=lambda:maxin(pagemor))
        baton4.place(x=721,y=35)

        tnt1=StringVar()
        tnt2=StringVar()
        tnt3=StringVar()
        tnt4=StringVar()
        tnt5=StringVar()
        tnt6=StringVar()
        tnt7=StringVar()
        tnt8=StringVar()
        tnt9=StringVar()

        label2= Label(pagesix,text= "Worker ID",bg= "white",fg= "blue",font="Times 16")
        label2.place(x=150,y=150)
        entry110=Entry(pagesix,width=17,bg="white",fg="black",font="Times 15",bd=3,relief="ridge",textvariable=tnt1)
        entry110.place(x=260,y=150)


        label2= Label(pagesix,text= "Marital Status",bg= "white",fg= "blue",font= "Times 16")
        label2.place(x=500,y=150)
        entry120=Entry(pagesix,width=17,bg="white",fg="black",font="Times 15",bd=3,relief="ridge",textvariable=tnt2)
        entry120.place(x=630,y=150)


        label2= Label(pagesix,text= "First Name",bg= "white",fg= "blue",font= "Times 16")
        label2.place(x=150,y=210)
        entry130=Entry(pagesix,width=17,bg="white",fg="black",font="Times 15",bd=3,relief="ridge",textvariable=tnt3)
        entry130.place(x=260,y=210)


        label2= Label(pagesix,text= "Date of Birth",bg= "white",fg= "blue",font= "Times 16")
        label2.place(x=500,y=210)
        entry140=Entry(pagesix,width=17,bg="white",fg="black",font="Times 15",bd=3,relief="ridge",textvariable=tnt4)
        entry140.place(x=630,y=210)


        label2= Label(pagesix,text= "Last Name",bg= "white",fg= "blue",font= "Times 16")
        label2.place(x=150,y=270)
        entry150=Entry(pagesix,width=17,bg="white",fg="black",font="Times 15",bd=3,relief="ridge",textvariable=tnt5)
        entry150.place(x=260,y=270)

        label2= Label(pagesix,text= "Residence",bg= "white",fg= "blue",font= "Times 16")
        label2.place(x=500,y=270)
        entry160=Entry(pagesix,width=17,bg="white",fg="black",font="Times 15",bd=3,relief="ridge",textvariable=tnt6)
        entry160.place(x=630,y=270)

        label4=Checkbutton(pagesix,text="Male",bg ="white",fg= "blue",font="Times 15")
        label4.place(x=150,y=330)

        check=Checkbutton(pagesix,text="Female",bg ="white",fg= "blue",font="Times 15")
        check.place(x=260,y=330)


        label2= Label(pagesix,text= "Department",bg= "white",fg= "blue",font= "Times 16")
        label2.place(x=500,y=330)
        entry180=Entry(pagesix,width=17,bg="white",fg="black",font="Times 15",bd=3,relief="ridge",textvariable=tnt7)
        entry180.place(x=630,y=330)


        label2= Label(pagesix,text= "Nationality",bg= "white",fg= "blue",font= "Times 16")
        label2.place(x=150,y=390)
        entry190= Entry(pagesix,width=17,bg="white",fg="black",font="Times 15",relief="ridge",bd=3,textvariable=tnt8)
        entry190.place(x=260,y=390)


        label2= Label(pagesix,text= "Education level",bg= "white",fg= "blue",font= "Times 16")
        label2.place(x=480,y=390)
        entry101=Entry(pagesix,width=17,bg="white",fg="black",font="Times 15",relief="ridge",bd=3,textvariable=tnt9)
        entry101.place(x=630,y=390)

        label2= Label(pagesix,text= "Comment",bg= "white",fg= "blue",font= "Times 16 bold")
        label2.place(x=62,y=450)
        
        text1= Text(pagesix,width=150,height=10,bg="white",fg="black",font="Times 10",bd=3,relief="ridge")
        text1.place(x=60,y=480)

        def ansa():
            if entry110.get()=="" or entry120.get()=="" or entry130.get()=="" or entry140.get()=="" or entry150.get()=="" or entry160.get()=="" or entry180.get()=="" or entry190.get()=="" or entry101.get()=="":
                print("Please enter all required details in the fields provided")
                label2= Label(pagesix,text="Please enter all required details in the fields provided",bg="white",fg="red",font= "Times 13")
                label2.place(x=400,y=420)
                
            else:
                waks=tnt1.get()
                fnem=tnt2.get()
                lnem=tnt3.get()
                nation=tnt4.get()
                mstus=tnt5.get()
                dobth=tnt6.get()
                resd=tnt7.get()
                dept=tnt8.get()
                educ=tnt9.get()

                entry110.delete(0,END)
                entry120.delete(0,END)
                entry130.delete(0,END)
                entry140.delete(0,END)
                entry150.delete(0,END)
                entry160.delete(0,END)
                entry180.delete(0,END)
                entry190.delete(0,END)
                entry101.delete(0,END)

                sqra="INSERT INTO Staff(workerid,Fname,Lname,nationality,mstatus,dob,resdnce,departmnt,Education) VALUES(?,?,?,?,?,?,?,?,?)"
                c.execute(sqra,(waks,fnem,lnem,nation,mstus,dobth,resd,dept,educ))
                conn.commit()
                
                
                tkinter.messagebox.showinfo("Success","Your details were successfully \nentered into the database")

        def can():
            waks=tnt1.get()
            sw=("DELETE FROM Staff WHERE workerid=?")
            c.execute(sw,[(waks)])
            conn.commit()
            tkinter.messagebox.askyesno("Warning","Details will be Deleted")

        
        baton=Button(pagesix,text="Save",width=6,font="Times 13 bold",bg="white",fg="maroon",command=ansa)
        baton.place(x=150,y=650)
        baton=Button(pagesix,text="Update",width=6,font="Times 13 bold",bg="white",fg="maroon")
        baton.place(x=450,y=650)
        baton=Button(pagesix,text="Delete",width=6,font="Times 13 bold",bg="white",fg="maroon",command=can)
        baton.place(x=750,y=650)
        
        xx=Button(pagesix,width=8,text="Log Out",font="Times 12 bold",bg="white",fg="blue",command=lambda:main(frame1))
        xx.place(x=900,y=660)



        ##View
        frame2=Frame(pageseven,width=2000,height=80,bg="light blue")
        frame2.place(x=0,y=0)
        
        baton=Button(pageseven,text="Create Accounts",bg="white",fg="green",font="Times 17 bold",width=16,command=lambda:maxin(create_frame))
        baton.place(x=70,y=35)
        baton2=Button(pageseven,text="Staff",width=16,bg="white",fg="green",font="Times 17 bold",command=lambda:maxin(pagesix))
        baton2.place(x=287,y=35)
        baton3=Button(pageseven,text="View Records",width=16,bg="white",fg="red",font="Times 17 bold")
        baton3.place(x=504,y=35)
        baton4=Button(pageseven,text="Mortury",width=16,bg="white",fg="green",font="Times 17 bold",command=lambda:maxin(pagemor))
        baton4.place(x=721,y=35)


        def nowa():
            frameb=Frame(window,width=2200,height=740)
            frameb.grid(row=0,column=0,sticky="news")
            
            image14 = PhotoImage(file="waks.png")
            w = image14.width()
            h = image14.height()
            window.geometry("%dx%d+0+0" % (w, h))
            panel4 =Label(frameb, image=image14)
            panel4.place(x=0,y=120)

            panel4.image = image14
            
            baton=Button(frameb,text="Back",fg="white",bg="blue",font="Times 14",command=lambda:maxin(pageseven))
            baton.place(x=20,y=10)

            labelz=Label(frameb,text="Name",width=6,font="Times 16",bg="white",fg="black",relief="flat",bd=3)
            labelz.place(x=312,y=81)
            entrwki=Entry(frameb,width=26,font="Times 18",bg="white",fg="black",relief="ridge",bd=3)
            entrwki.place(x=390,y=80)

            def rund44():
                try:
                    if entrwki.get()=="":
                        lablezs=Label(frameb,text="Please fill in the space provided ????",fg="red",font="Times 14",bg="white")
                        lablezs.place(x=310,y=118)
                        print("Please fill in the space provided ????")
                    else:
                        sqba=("SELECT * FROM inpatient WHERE fname=?")
                        c.execute(sqba,([entrwki.get()]))
                        rowsza =c.fetchall()
                        for roxyva in rowsza:
                            print(roxyva)
                        text90=Text(frameb,width=123,height=20,bg="white")
                        text90.place(x=70,y=120)
                        text90.insert(INSERT,roxyva)
                except UnboundLocalError:
                    lablezd=Label(frameb,text="We are sorry\nWe don't have such records here!!!",fg="red",font="Times 15",bg="white")
                    lablezd.place(x=380,y=118)
                    print("No Such records")
            def perform():
                sqba=("SELECT * FROM inpatient WHERE fname=?")
                c.execute(sqba,([entrwki.get()]))
                rowsza =c.fetchall()
                for roxyvar in rowsza:
                    print(roxyvar[3])
                a=str(roxyvar[3])
                b=str(roxyvar[4])
                window1 =Tk()
                window1.title("Records")
                window1.geometry("1800x740")
                window.configure(bg="white")
                e=Entry(window1,width=12,background="white",foreground="black",font="Times 18")
                e.place(x=265,y=580)
                def saveFile():
                    try:
                        with open(e.get()+'.txt', 'w') as note: 
                            text = text_entry.get("1.0", 'end-1c') 
                            note.write(text)
                            tkinter.messagebox.showinfo("Success","Document has been saved to your desktop")
                            e.delete(0,END)
                    except IOError as err:
                        print("File error " + str(err))
                        
                text_entry = Text(window1,width=125,height=35,)
                text_entry.grid(column=0, row=0)
                text_entry.insert(INSERT,"\n\n           ")
                text_entry.insert(INSERT,"                "+"First Name: "+roxyvar[1])
                text_entry.insert(INSERT,"                "+"Last Name: "+roxyvar[2])
                text_entry.insert(INSERT,"\n\n           ")
                text_entry.insert(INSERT,"Age: "+a+"                   ")
                text_entry.insert(INSERT,"Weight: "+b)
                
                

                action = Button(window1, text="Save",font="Times 12",command=saveFile,width=10) 
                action.place(x=435,y=578)
                lab=Label(window1,text="File name:",font="Times 16",bg="white",fg="blue",width=8)
                lab.place(x=150,y=580)
                text_entry.focus()
                

            baton=Button(frameb,text="Make a Report",width=20,fg="maroon",bg="white",font="Times 13 italic",command=perform)
            baton.place(x=400,y=650)
                
            baton5=Button(frameb,text="Search",width=8,font="Times 13",bg="grey",fg="white",relief="groove",command=rund44)
            baton5.place(x=709,y=80)

            

            
        Inpatient_baton=Button(pageseven,text="In patient",width=8,font="Times 16",bg="red",fg="white",command=nowa)
        Inpatient_baton.place(x=115,y=120)
###################################################

        def nowz():
            frameba=Frame(window,width=2200,height=740)
            frameba.grid(row=0,column=0,sticky="news")
            baton=Button(frameba,text="Back",fg="white",bg="blue",font="Times 14",command=lambda:maxin(pageseven))
            baton.place(x=20,y=10)

            label=Label(frameba,text="Name",width=6,font="Times 16",bg="white",fg="black",relief="flat",bd=3)
            label.place(x=312,y=81)

            entryd=Entry(frameba,width=26,font="Times 18",bg="white",fg="black",relief="ridge",bd=3)
            entryd.place(x=390,y=80)

            def rund1():
                try:
                    if entryd.get()=="":
                        lablezs=Label(frameba,text="Please fill in the space provided ????",fg="red",font="Times 14",bg="white")
                        lablezs.place(x=310,y=118)
                        print("Please fill in the space provided ????")
                    else:
                        sqba=("SELECT * FROM Outpatient WHERE fname=?")
                        c.execute(sqba,([entryd.get()]))
                        rowsz =c.fetchall()
                        for roxyv in rowsz:
                            print(roxyv)
                           
                        baton=Button(frameba,text="Back",fg="white",bg="blue",font="Times 14",command=lambda:maxin(pageseven))
                        baton.place(x=20,y=10)
                        text90=Text(frameba,width=123,height=20,bg="white")
                        text90.place(x=70,y=120)
                        text90.insert(INSERT,roxyv)
                except UnboundLocalError:
                    lablezd=Label(frameba,text="We are sorry\nWe don't have such records here!!!",fg="red",font="Times 15",bg="white")
                    lablezd.place(x=340,y=118)
                    print("No Such records")
            def perform():
                window1 =Tk()
                window1.title("Records")
                window1.geometry("1800x740")
                window.configure(bg="white")

                e=Entry(window1,width=12,background="white",foreground="black",font="Times 18")
                e.place(x=265,y=580)
                def saveFile():
                    try:
                        with open(e.get()+'.txt', 'w') as note: 
                            text = text_entry.get("1.0", 'end-1c') 
                            note.write(text)
                            tkinter.messagebox.showinfo("Success","Document has been saved to your desktop")
                            window1.destroy
                    except IOError as err:
                        print("File error " + str(err))
                        
                text_entry = Text(window1,width=125,height=35,)
                text_entry.grid(column=0, row=0) 

                action = Button(window1, text="Save",font="Times 12",command=saveFile,width=10) 
                action.place(x=435,y=578)
                lab=Label(window1,text="File name:",font="Times 16",bg="white",fg="blue",width=8)
                lab.place(x=150,y=580)

                text_entry.focus()
                window1.mainloop()

            baton=Button(frameb,text="Make a Report",width=20,fg="maroon",bg="white",font="Times 13 italic",command=perform)
            baton.place(x=400,y=650)



            baton=Button(frameba,text="Search",width=8,font="Times 13",bg="grey",fg="white",relief="groove",command=rund1)
            baton.place(x=709,y=80)
            
        Outpatient_baton=Button(pageseven,text="Out patient",width=8,font="Times 16",bg="red",fg="white",command=nowz)
        Outpatient_baton.place(x=115,y=200)
#############################################################

        def nowzara():
            frameba=Frame(window,width=2200,height=740)
            frameba.grid(row=0,column=0,sticky="news")
            baton=Button(frameba,text="Back",fg="white",bg="blue",font="Times 14",command=lambda:maxin(pageseven))
            baton.place(x=20,y=10)

            label=Label(frameba,text="Name",width=7,font="Times 16",bg="white",fg="black",relief="flat",bd=3)
            label.place(x=303,y=81)
                    
            entryz=Entry(frameba,width=26,font="Times 18",bg="white",fg="black",relief="ridge",bd=3)
            entryz.place(x=390,y=80)
            def rund3():
                try:
                    if entryz.get()=="":
                        lablezs=Label(frameba,text="Please fill in the space provided ????",fg="red",font="Times 14",bg="white")
                        lablezs.place(x=280,y=118)
                        print("Please fill in the space provided ????")
                    else:
                        sqba=("SELECT * FROM Labs WHERE names=?")
                        c.execute(sqba,([entryz.get()]))
                        rowsz =c.fetchall()
                        for roxyv in rowsz:
                            print(roxyv)
                           
                        baton=Button(frameba,text="Back",fg="white",bg="blue",font="Times 14",command=lambda:maxin(pageseven))
                        baton.place(x=20,y=10)
                        text90=Text(frameba,width=123,height=20,bg="white")
                        text90.place(x=80,y=120)
                        text90.insert(INSERT,roxyv)
                except UnboundLocalError:
                    lablezd=Label(frameba,text="We are sorry\nWe don't have such records here!!!",fg="red",font="Times 15",bg="white")
                    lablezd.place(x=340,y=118)
                    print("No Such records")

            def perform():
                sqba=("SELECT * FROM Labs WHERE names=?")
                c.execute(sqba,([entryz.get()]))
                rowsz =c.fetchall()
                for roxyv in rowsz:
                    print(roxyv)
                w=str(roxyv[1])
                window1 =Tk()
                window1.title("Records")
                window1.geometry("1800x740")
                window.configure(bg="white")

                e=Entry(window1,width=12,background="white",foreground="black",font="Times 18")
                e.place(x=265,y=580)
                def saveFile():
                    try:
                        with open(e.get()+'.txt', 'w') as note: 
                            text = text_entry.get("1.0", 'end-1c') 
                            note.write(text)
                            tkinter.messagebox.showinfo("Success","Document has been saved to your desktop")
                            window1.destroy
                    except IOError as err:
                        print("File error " + str(err))
                        
                text_entry = Text(window1,width=125,height=35,)
                text_entry.grid(column=0, row=0)

                text_entry.insert(INSERT,"                          ")
                text_entry.insert(INSERT,"Laboratory  Form   ")
                text_entry.insert(INSERT,"\n\n\nNames:"+"   "+roxyv[0])
                text_entry.insert(INSERT,"                  ")
                text_entry.insert(INSERT,"Age:"+"   "+w)
                text_entry.insert(INSERT,"\n\nAddress:"+"   "+roxyv[2])
                text_entry.insert(INSERT,"                ")
                text_entry.insert(INSERT,"Tests against:"+"   "+roxyv[3])
                text_entry.insert(INSERT,"                   ")
                text_entry.insert(INSERT,"\n\n\n                           ")
                text_entry.insert(INSERT,"Clinical Notes")
                text_entry.insert(INSERT,"\n............................................................................")
                text_entry.insert(INSERT,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n............................................................................")
                
                

                action = Button(window1, text="Save",font="Times 12",command=saveFile,width=10) 
                action.place(x=435,y=578)
                lab=Label(window1,text="File name:",font="Times 16",bg="white",fg="blue",width=8)
                lab.place(x=150,y=580)

                text_entry.focus()
                window1.mainloop()

            baton=Button(frameba,text="Make a Report",width=20,fg="maroon",bg="white",font="Times 13 italic",command=perform)
            baton.place(x=400,y=650)

            baton=Button(frameba,text="Search",width=8,font="Times 13",bg="grey",fg="white",relief="groove",command=rund3)
            baton.place(x=709,y=80)

        Mangt_baton=Button(pageseven,text="Laboratory",width=8,font="Times 16",bg="red",fg="white",command=nowzara)
        Mangt_baton.place(x=115,y=280)
########################################################################


        def nowzar():
            frameba=Frame(window,width=2200,height=740)
            frameba.grid(row=0,column=0,sticky="news")
            baton=Button(frameba,text="Back",fg="white",bg="blue",font="Times 14",command=lambda:maxin(pageseven))
            baton.place(x=20,y=10)

            label=Label(frameba,text="Patient ID",width=7,font="Times 16",bg="white",fg="black",relief="flat",bd=3)
            label.place(x=303,y=81)
                    
            entryv=Entry(frameba,width=26,font="Times 18",bg="white",fg="black",relief="ridge",bd=3)
            entryv.place(x=390,y=80)
            def rund2():
                try:
                    if entryv.get()=="":
                        lablezs=Label(frameba,text="Please fill in the space provided ????",fg="red",font="Times 14",bg="white")
                        lablezs.place(x=280,y=118)
                        print("Please fill in the space provided ????")
                    else:
                        sqba=("SELECT * FROM Bills WHERE patid=?")
                        c.execute(sqba,([entryv.get()]))
                        rowsz =c.fetchall()
                        for roxyv in rowsz:
                            print(roxyv)
                           
                        baton=Button(frameba,text="Back",fg="white",bg="blue",font="Times 14",command=lambda:maxin(pageseven))
                        baton.place(x=20,y=10)
                        text90=Text(frameba,width=123,height=20,bg="white")
                        text90.place(x=80,y=110)
                        text90.insert(INSERT,roxyv)
                except UnboundLocalError:
                    lablezd=Label(frameba,text="We are sorry\nWe don't have such records here!!!",fg="red",font="Times 15",bg="white")
                    lablezd.place(x=340,y=118)
                    print("No Such records")

            def perform():
                window1 =Tk()
                window1.title("Records")
                window1.geometry("1800x740")
                window.configure(bg="white")

                e=Entry(window1,width=12,background="white",foreground="black",font="Times 18")
                e.place(x=265,y=580)
                def saveFile():
                    try:
                        with open(e.get()+'.txt', 'w') as note: 
                            text = text_entry.get("1.0", 'end-1c') 
                            note.write(text)
                            tkinter.messagebox.showinfo("Success","Document has been saved to your desktop")
                            window1.destroy
                    except IOError as err:
                        print("File error " + str(err))
                        
                text_entry = Text(window1,width=125,height=35,)
                text_entry.grid(column=0, row=0)
                text_entry.insert(INSERT,"                          ")
                text_entry.insert(INSERT,"Patient Bill Form   ")
                text_entry.insert(INSERT,"\n\n\nPatient Name:"+"  ")
                text_entry.insert(INSERT,"\n\n\nPatient Address:"+"  ")
                text_entry.insert(INSERT,"\n\n\nDate of Bill"+"       ")
                text_entry.insert(INSERT,"Service details"+"   ")
                text_entry.insert(INSERT,"Total Billing Amount"+"   ")
                text_entry.insert(INSERT,"                              ")

                action = Button(window1, text="Save",font="Times 12",command=saveFile,width=10) 
                action.place(x=435,y=578)
                lab=Label(window1,text="File name:",font="Times 16",bg="white",fg="blue",width=8)
                lab.place(x=150,y=580)

                text_entry.focus()
                window1.mainloop()

            baton=Button(frameba,text="Make a Report",width=20,fg="maroon",bg="white",font="Times 13 italic",command=perform)
            baton.place(x=400,y=650)

            baton=Button(frameba,text="Search",width=8,font="Times 13",bg="grey",fg="white",relief="groove",command=rund2)
            baton.place(x=709,y=80)

            
        Room_baton=Button(pageseven,text="Bill",width=8,font="Times 16",bg="red",fg="white",command=nowzar)
        Room_baton.place(x=115,y=360)
###############################################
        def nowsarh():
            frameba=Frame(window,width=2200,height=740)
            frameba.grid(row=0,column=0,sticky="news")

            image19 = PhotoImage(file="waks.png")
            w = image19.width()
            h = image19.height()
            window.geometry("%dx%d+0+0" % (w, h))
            panel4 =Label(frameba, image=image19)
            panel4.place(x=0,y=120)

            panel4.image = image19
            
            baton=Button(frameba,text="Back",fg="white",bg="blue",font="Times 14",command=lambda:maxin(pageseven))
            baton.place(x=20,y=10)

            label=Label(frameba,text="Name",width=7,font="Times 16",bg="white",fg="black",relief="flat",bd=3)
            label.place(x=303,y=81)
                    
            entryvsv=Entry(frameba,width=26,font="Times 18",bg="white",fg="black",relief="ridge",bd=3)
            entryvsv.place(x=390,y=80)
            def rund6():
                try:
                    if entryvsv.get()=="":
                        lablezs=Label(frameba,text="Please fill in the space provided ????",fg="red",font="Times 14",bg="white")
                        lablezs.place(x=280,y=118)
                        print("Please fill in the space provided ????")
                    else:
                        sqba=("SELECT * FROM Immune WHERE patientname=?")
                        c.execute(sqba,([entryvsv.get()]))
                        rowsz =c.fetchall()
                        for roxyv in rowsz:
                            print(roxyv)
                           
                        baton=Button(frameba,text="Back",fg="white",bg="blue",font="Times 14",command=lambda:maxin(pageseven))
                        baton.place(x=20,y=10)
                        text90=Text(frameba,width=123,height=20,bg="white")
                        text90.place(x=80,y=120)
                        text90.insert(INSERT,roxyv)
                except UnboundLocalError:
                    lablezd=Label(frameba,text="We are sorry\nWe don't have such records here!!!",fg="red",font="Times 15",bg="white")
                    lablezd.place(x=340,y=118)
                    print("No Such records")

            def perform():
                sqba=("SELECT * FROM Immune WHERE patientname=?")
                c.execute(sqba,([entryvsv.get()]))
                rowsz =c.fetchall()
                for roxyv in rowsz:
                    print(roxyv)
                w=str(roxyv[1])
                window1 =Tk()
                window1.title("Records")
                window1.geometry("1800x740")
                window.configure(bg="white")

                e=Entry(window1,width=12,background="white",foreground="black",font="Times 18")
                e.place(x=265,y=580)
                def saveFile():
                    try:
                        with open(e.get()+'.txt', 'w') as note: 
                            text = text_entry.get("1.0", 'end-1c') 
                            note.write(text)
                            tkinter.messagebox.showinfo("Success","Document has been saved to your desktop")
                            window1.destroy
                    except IOError as err:
                        print("File error " + str(err))
                        
                text_entry = Text(window1,width=125,height=35)
                text_entry.grid(column=0, row=0)
                text_entry.insert(INSERT,"                          ")
                text_entry.insert(INSERT,"Immunisation  Form   ")
                text_entry.insert(INSERT,"\n\n\nName of Child:"+"  "+roxyv[0])
                text_entry.insert(INSERT,"                              ")
                text_entry.insert(INSERT,"Age:"+"   "+w)
                text_entry.insert(INSERT,"\n\nName of Parent:"+"   "+roxyv[2])
                text_entry.insert(INSERT,"\n\nAddress:"+"   "+roxyv[3])
                text_entry.insert(INSERT,"                              ")
                text_entry.insert(INSERT,"Immunisation against:"+"   "+roxyv[4])
                text_entry.insert(INSERT,"                   ")
                text_entry.insert(INSERT,"\n\n\n                       ")
                text_entry.insert(INSERT,"Date each Dose was given")
                text_entry.insert(INSERT,"\n\nVaccine"+"           ")
                text_entry.insert(INSERT,"  "+"1st"+"        ")
                text_entry.insert(INSERT,"  "+"2nd"+"        ")
                text_entry.insert(INSERT," "+"3rd"+"        ")
                text_entry.insert(INSERT," "+"4th"+"        ")
                text_entry.insert(INSERT," "+"5th"+"        ")
                text_entry.insert(INSERT,"\n\nMeasles"+"           ")
                text_entry.insert(INSERT,"........")
                text_entry.insert(INSERT,"    "+"........")
                text_entry.insert(INSERT,"    "+"........")
                text_entry.insert(INSERT,"    "+"........")
                text_entry.insert(INSERT,"    "+"........")
                text_entry.insert(INSERT,"\n\nPolio"+"             ")
                text_entry.insert(INSERT,"........")
                text_entry.insert(INSERT,"    "+"........")
                text_entry.insert(INSERT,"    "+"........")
                text_entry.insert(INSERT,"    "+"........")
                text_entry.insert(INSERT,"    "+"........")
                text_entry.insert(INSERT,"\n\nHepatitis B"+"       ")
                text_entry.insert(INSERT,"........")
                text_entry.insert(INSERT,"    "+"........")
                text_entry.insert(INSERT,"    "+"........")
                text_entry.insert(INSERT,"    "+"........")
                text_entry.insert(INSERT,"    "+"........")
                text_entry.insert(INSERT,"\n\n\nNext Immunisation date  is due:"+"           ")
                text_entry.insert(INSERT,"\n\nMeasles"+"        ")
                text_entry.insert(INSERT,"...........................")
                text_entry.insert(INSERT,"\n\nPolio"+"          ")
                text_entry.insert(INSERT,"...........................")
                text_entry.insert(INSERT,"\n\nHepatitis B"+"    ")
                text_entry.insert(INSERT,"...........................")
                text_entry.insert(INSERT,"\n\n\n\n\n\n      ")
                text_entry.insert(INSERT,"Stamp:")
                text_entry.insert(INSERT,"                                  ")
                text_entry.insert(INSERT,"Signature of Health Provider:")
                text_entry.insert(INSERT,"\n\n\n\n......................")
                text_entry.insert(INSERT,"                      ")
                text_entry.insert(INSERT,"..............................")
                
                

                action = Button(window1, text="Save",font="Times 12",command=saveFile,width=10) 
                action.place(x=435,y=578)
                lab=Label(window1,text="File name:",font="Times 16",bg="white",fg="blue",width=8)
                lab.place(x=150,y=580)

                text_entry.focus()
                window1.mainloop()

            baton=Button(frameba,text="Make a Report",width=20,fg="maroon",bg="white",font="Times 13 italic",command=perform)
            baton.place(x=400,y=650)

            baton=Button(frameba,text="Search",width=8,font="Times 13",bg="grey",fg="white",relief="groove",command=rund6)
            baton.place(x=709,y=80)


        
        Bill_baton=Button(pageseven,text="Immunisation",width=8,font="Times 16",bg="red",fg="white",command=nowsarh)
        Bill_baton.place(x=699,y=120)
###############################################
        def nowsar():
            frameba=Frame(window,width=2200,height=740)
            frameba.grid(row=0,column=0,sticky="news")

            image19 = PhotoImage(file="waks.png")
            w = image19.width()
            h = image19.height()
            window.geometry("%dx%d+0+0" % (w, h))
            panel4 =Label(frameba, image=image19)
            panel4.place(x=0,y=120)

            panel4.image = image19
            
            baton=Button(frameba,text="Back",fg="white",bg="blue",font="Times 14",command=lambda:maxin(pageseven))
            baton.place(x=20,y=10)

            label=Label(frameba,text="Name",width=7,font="Times 16",bg="white",fg="black",relief="flat",bd=3)
            label.place(x=303,y=81)
                    
            entryvsv=Entry(frameba,width=26,font="Times 18",bg="white",fg="black",relief="ridge",bd=3)
            entryvsv.place(x=390,y=80)
            def rund6():
                try:
                    if entryvsv.get()=="":
                        lablezs=Label(frameba,text="Please fill in the space provided ????",fg="red",font="Times 14",bg="white")
                        lablezs.place(x=280,y=118)
                        print("Please fill in the space provided ????")
                    else:
                        sqba=("SELECT * FROM Mortury WHERE Name=?")
                        c.execute(sqba,([entryvsv.get()]))
                        rowsz =c.fetchall()
                        for roxyv in rowsz:
                            print(roxyv)
                           
                        baton=Button(frameba,text="Back",fg="white",bg="blue",font="Times 14",command=lambda:maxin(pageseven))
                        baton.place(x=20,y=10)
                        text90=Text(frameba,width=123,height=20,bg="white")
                        text90.place(x=80,y=120)
                        text90.insert(INSERT,roxyv)
                except UnboundLocalError:
                    lablezd=Label(frameba,text="We are sorry\nWe don't have such records here!!!",fg="red",font="Times 15",bg="white")
                    lablezd.place(x=340,y=118)
                    print("No Such records")

            def perform():
                sqba=("SELECT * FROM Mortury WHERE Name=?")
                c.execute(sqba,([entryvsv.get()]))
                rowsz =c.fetchall()
                for roxyv in rowsz:
                    print(roxyv)
                w=str(roxyv[5])
                window1 =Tk()
                window1.title("Records")
                window1.geometry("1800x740")
                window.configure(bg="white")

                e=Entry(window1,width=12,background="white",foreground="black",font="Times 18")
                e.place(x=265,y=580)
                def saveFile():
                    try:
                        with open(e.get()+'.txt', 'w') as note: 
                            text = text_entry.get("1.0", 'end-1c') 
                            note.write(text)
                            tkinter.messagebox.showinfo("Success","Document has been saved to your desktop")
                            window1.destroy
                    except IOError as err:
                        print("File error " + str(err))
                text_entry = Text(window1,width=125,height=35,)
                text_entry.grid(column=0, row=0) 
                text_entry.insert(INSERT,"                          ")
                text_entry.insert(INSERT,"Death Report Summary   ")
                text_entry.insert(INSERT,"\n\n\nFrom")
                text_entry.insert(INSERT,"                                              ")
                text_entry.insert(INSERT,"Patient ID:"+"  "+roxyv[2])
                text_entry.insert(INSERT,"\n                        ")
                text_entry.insert(INSERT,"\n        ")
                text_entry.insert(INSERT,"Doctor InCharge:"+"  "+roxyv[1])
                text_entry.insert(INSERT,"\n\n\n\nTo")
                text_entry.insert(INSERT,"\n        ")
                text_entry.insert(INSERT,"Family of:"+"   "+roxyv[0])
                text_entry.insert(INSERT,"                   ")
                text_entry.insert(INSERT,"Aged:"+"  "+w)
                text_entry.insert(INSERT,"\n\n\n\nDate of Death:"+"  "+roxyv[3])
                text_entry.insert(INSERT,"                   ")
                text_entry.insert(INSERT,"Cause of Death:"+"  "+roxyv[4])
                text_entry.insert(INSERT,"\n\n\n\n\n\n      ")
                text_entry.insert(INSERT,"Stamp:")
                text_entry.insert(INSERT,"                                  ")
                text_entry.insert(INSERT,"Released by:")
                text_entry.insert(INSERT,"\n\n\n\n......................")
                text_entry.insert(INSERT,"                      ")
                text_entry.insert(INSERT,"...........................")

                action = Button(window1, text="Save",font="Times 12",command=saveFile,width=10) 
                action.place(x=435,y=578)
                lab=Label(window1,text="File name:",font="Times 16",bg="white",fg="blue",width=8)
                lab.place(x=150,y=580)

                text_entry.focus()
                window1.mainloop()

            baton=Button(frameba,text="Make a Report",width=20,fg="maroon",bg="white",font="Times 13 italic",command=perform)
            baton.place(x=400,y=650)

            baton=Button(frameba,text="Search",width=8,font="Times 13",bg="grey",fg="white",relief="groove",command=rund6)
            baton.place(x=709,y=80)


        Mortury_baton=Button(pageseven,text="Mortury",width=8,font="Times 16",bg="red",fg="white",command=nowsar)
        Mortury_baton.place(x=115,y=520)
#####################################

        def nowzarar():
            frameba=Frame(window,width=2200,height=740)
            frameba.grid(row=0,column=0,sticky="news")
            baton=Button(frameba,text="Back",fg="white",bg="blue",font="Times 14",command=lambda:maxin(pageseven))
            baton.place(x=20,y=10)

            label=Label(frameba,text="Patient ID",width=7,font="Times 16",bg="white",fg="black",relief="flat",bd=3)
            label.place(x=303,y=81)
                    
            entryvs=Entry(frameba,width=26,font="Times 18",bg="white",fg="black",relief="ridge",bd=3)
            entryvs.place(x=390,y=80)
            def rund6():
                try:
                    if entryvs.get()=="":
                        lablezs=Label(frameba,text="Please fill in the space provided ????",fg="red",font="Times 14",bg="white")
                        lablezs.place(x=280,y=118)
                        print("Please fill in the space provided ????")
                    else:
                        sqba=("SELECT * FROM Dental WHERE patientid=?")
                        c.execute(sqba,([entryvs.get()]))
                        rowsz =c.fetchall()
                        for roxyv in rowsz:
                            print(roxyv)
                           
                        baton=Button(frameba,text="Back",fg="white",bg="blue",font="Times 14",command=lambda:maxin(pageseven))
                        baton.place(x=20,y=10)
                        text90=Text(frameba,width=123,height=20,bg="white")
                        text90.place(x=80,y=120)
                        text90.insert(INSERT,roxyv)
                except UnboundLocalError:
                    lablezd=Label(frameba,text="We are sorry\nWe don't have such records here!!!",fg="red",font="Times 15",bg="white")
                    lablezd.place(x=340,y=118)
                    print("No Such records")

            def perform():
                window1 =Tk()
                window1.title("Records")
                window1.geometry("1800x740")
                window.configure(bg="white")

                e=Entry(window1,width=12,background="white",foreground="black",font="Times 18")
                e.place(x=265,y=580)
                def saveFile():
                    try:
                        with open(e.get()+'.txt', 'w') as note: 
                            text = text_entry.get("1.0", 'end-1c') 
                            note.write(text)
                            tkinter.messagebox.showinfo("Success","Document has been saved to your desktop")
                            window1.destroy
                    except IOError as err:
                        print("File error " + str(err))
                        
                text_entry = Text(window1,width=125,height=35,)
                text_entry.grid(column=0, row=0) 

                action = Button(window1, text="Save",font="Times 12",command=saveFile,width=10) 
                action.place(x=435,y=578)
                lab=Label(window1,text="File name:",font="Times 16",bg="white",fg="blue",width=8)
                lab.place(x=150,y=580)

                text_entry.focus()
                window1.mainloop()

            baton=Button(frameb,text="Make a Report",width=20,fg="maroon",bg="white",font="Times 13 italic",command=perform)
            baton.place(x=400,y=650)

            baton=Button(frameba,text="Search",width=8,font="Times 13",bg="grey",fg="white",relief="groove",command=rund6)
            baton.place(x=709,y=80)

        
        Dent_baton=Button(pageseven,text="Dental",width=8,font="Times 16",bg="red",fg="white",command=nowzarar)
        Dent_baton.place(x=115,y=440)
        
        xx=Button(pageseven,width=8,text="Log Out",font="Times 12 bold",bg="white",fg="blue",command=lambda:main(frame1))
        xx.place(x=900,y=660)



        ##pagemortury
        frame2=Frame(pagemor,width=2000,height=80,bg="light blue")
        frame2.place(x=0,y=0)
        
        baton=Button(pagemor,text="Create Accounts",bg="white",fg="green",font="Times 17 bold",width=16,command=lambda:maxin(create_frame))
        baton.place(x=70,y=35)
        baton2=Button(pagemor,text="Staff",width=16,bg="white",fg="green",font="Times 17 bold",command=lambda:maxin(pagesix))
        baton2.place(x=287,y=35)
        baton3=Button(pagemor,text="View Records",width=16,bg="white",fg="green",font="Times 17 bold",command=lambda:maxin(pageseven))
        baton3.place(x=504,y=35)
        baton4=Button(pagemor,text="Mortury",width=16,bg="white",fg="red",font="Times 17 bold")
        baton4.place(x=721,y=35)
        


        label=Label(pagemor,text="Name:",width=7,font="Times 16",bg="white",fg="blue")
        label.place(x=230,y=160)
        label=Label(pagemor,text="Doctor's Name:",width=8,font="Times 16",bg="white",fg="blue")
        label.place(x=230,y=280)
        label=Label(pagemor,text="Patient ID:",width=10,font="Times 16",bg="white",fg="blue")
        label.place(x=220,y=220)
        label=Label(pagemor,text="Date of Death:",width=10,font="Times 16",bg="white",fg="blue")
        label.place(x=204,y=340)
        label=Label(pagemor,text="Postmotem Tests:",width=16,font="Times 16",bg="white",fg="blue")
        label.place(x=155,y=400)
        label=Label(pagemor,text="Age:",width=5,font="Times 16",bg="white",fg="blue")
        label.place(x=550,y=160)
        
                

        tcvt1=StringVar()
        tcvt2=StringVar()
        tcvt3=StringVar()
        tcvt4=StringVar()
        tcvt5=StringVar()
        tcvt6=StringVar()
        
        entry111=Entry(pagemor,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tcvt1)
        entry111.place(x=320,y=160)
        entry121=Entry(pagemor,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tcvt2)
        entry121.place(x=380,y=280)
        entry131=Entry(pagemor,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tcvt3)
        entry131.place(x=340,y=220)
        entry141=Entry(pagemor,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tcvt4)
        entry141.place(x=340,y=340)
        entry151=Entry(pagemor,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tcvt5)
        entry151.place(x=340,y=400)
        entry161=Entry(pagemor,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tcvt6)
        entry161.place(x=650,y=160)


        label=Label(pagemor,text="Add Notes",width=10,font="Times 18 bold",bg="white",fg="blue")
        label.place(x=56,y=440)

        text1=Text(pagemor,width=80,height=7,font="Times 16",bg="white",fg="black",relief="ridge",bd=3)
        text1.place(x=60,y=468)
        def response():
            if entry111.get()=="" or entry121.get()=="" or entry131.get()=="" or entry141.get()=="" or entry151.get()=="":
                print("Please enter all required details in the fields provided")
                label2= Label(pagemor,text="Please enter all required details in the fields provided",bg="white",fg="red",font= "Times 13")
                label2.place(x=400,y=380)
            else:
                nem=tcvt1.get()
                wakd=tcvt2.get()
                pated=tcvt3.get()
                dodeath=tcvt4.get()
                postmotems=tcvt5.get()
                aged=tcvt6.get()

                entry111.delete(0,END)
                entry121.delete(0,END)
                entry131.delete(0,END)
                entry141.delete(0,END)
                entry151.delete(0,END)
                
                sgt="INSERT INTO Mortury(Name,Doctorname,patientid,DoD,Postmotem,Age) VALUES(?,?,?,?,?,?)"
                c.execute(sgt,(nem,wakd,pated,dodeath,postmotems,aged))
                conn.commit()
                
                tkinter.messagebox.showinfo("Success","Your details were successfully \nentered into the database")

        def can():
            nem=tcvt1.get()
            sw=("DELETE FROM Mortury WHERE nem=?")
            c.execute(sw,[(nem)])
            conn.commit()
            tkinter.messagebox.askyesno("Warning","Details will be Deleted")
            
        baton=Button(pagemor,text="Save",width=6,font="Times 13 bold",bg="white",fg="maroon",command=response,relief="raised")
        baton.place(x=150,y=650)
        baton=Button(pagemor,text="Update",width=6,font="Times 13 bold",bg="white",fg="maroon")
        baton.place(x=450,y=650)
        baton=Button(pagemor,text="Delete",width=6,font="Times 13 bold",bg="white",fg="maroon",command=can)
        baton.place(x=750,y=650)
        
        
        xx=Button(pagemor,width=8,text="Log Out",font="Times 12 bold",bg="white",fg="blue",command=lambda:main(frame1))
        xx.place(x=900,y=660)

        ######################################
        ##########save changes#########

        def callme():
            frame55=Frame(window,width=2000,height=740)
            frame55.grid(row=0,column=0,sticky="news")

            image90 = PhotoImage(file="waks.png")
            w = image90.width()
            h = image90.height()
            window.geometry("%dx%d+0+0" % (w, h))
            panel90 =Label(frame55, image=image90)
            panel90.place(x=0,y=0)

            panel90.image = image90

            label1=Label(frame55,text="Reset Your Passwords",font="Times 18",bg="white",fg="blue")
            label1.place(x=430,y=110)
            label2=Label(frame55,text="Previous ID",font="Times 17",bg="white",fg="blue")
            label2.place(x=310,y=230)
            label3=Label(frame55,text="New password",font="Times 17",bg="white",fg="blue")
            label3.place(x=300,y=290)
            label4=Label(frame55,text="Confirm password",font="Times 17",bg="white",fg="blue")
            label4.place(x=300,y=350)

            var=StringVar()
            bar=StringVar()
            dar=StringVar()

            entral1762=Entry(frame55,width=21,font="Times 18",bg="white",fg="black",relief="ridge",bd=3,textvariable=var)
            entral1762.place(x=480,y=230)
            entral2762=Entry(frame55,width=17,font="Courier 17",bg="white",fg="black",relief="ridge",bd=3,show="*",textvariable=bar)
            entral2762.place(x=480,y=290)
            entral3762=Entry(frame55,width=17,font="Courier 17",bg="white",fg="black",relief="ridge",bd=3,show="*",textvariable=dar)
            entral3762.place(x=480,y=350)
            fal=var.get()
            alk=bar.get()
            akl=dar.get()
    
            def responed():
                if len(entral2762.get())<8:
                    print("It's too short")
                    label4=Label(frame55,text="Password should cosist of more than 8 characters",font="Times 13",bg="white",fg="red")
                    label4.place(x=300,y=280)
                elif entral2762.get()!= entral3762.get():
                    label4=Label(frame55,text="Reconfirm your password",font="Times 13",bg="white",fg="red")
                    label4.place(x=300,y=300)
                else:
                    var1=entral1762.get()
                    var2=entral2762.get()
                    sql2=("UPDATE details SET password=? WHERE ID=?")
                    c.execute(sql2,(var2,var1))
                    conn.commit()
                    tkinter.messagebox.askyesno("Warning","Details will be updated")
      
            baton=Button(frame55,text="Save Changes",font="Times 14 bold",fg="maroon",bg="white",command=responed)
            baton.place(x=700,y=420)


            baton=Button(frame55,width=7,text="Back",font="Times 13 bold",fg="maroon",bg="white",command=lambda:maxin(create_frame))
            baton.place(x=10,y=30)

        ######Save Changes####################
        ######################################
        menu = Menu(create_frame)                          
        window.config(menu=menu)

        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)


        settingsmenu=Menu(menu)
        menu.add_cascade(label="Settings",menu=settingsmenu)

        helpmenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)

        filemenu.add_command(label="New", command=callback)
        filemenu.add_command(label="Open...", command=respond)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=window.destroy)

        settingsmenu.add_command(label="Password Reset", command=callme)
        
        helpmenu.add_command(label="About Us...", command=respond)
        
    elif userid in lista4 and paswad in lista2:
        print("Welcome")
        def remain(frame):
            frame.tkraise()
            
        pageone=Frame(window,width=2000,height=740,bg="white")
        pagetwo=Frame(window,width=2000,height=740,bg="white")
        pagethree=Frame(window,width=2000,height=740,bg="white")
        pagefour=Frame(window,width=2000,height=740,bg="white")
        pagefive=Frame(window,width=2000,height=740,bg="white")
        pagesixt=Frame(window,width=2000,height=740,bg="white")
        for framez in (pagesixt,pagefive,pagefour,pagethree,pagetwo,pageone):
            framez.grid(row=0,column=0,sticky="news")

        image5 = PhotoImage(file="waks.png")
        w = image5.width()
        h = image5.height()
        window.geometry("%dx%d+0+0" % (w, h))
        panel5 =Label(pageone, image=image5)
        panel5.place(x=0,y=80)

        panel5.image = image5

        image6 = PhotoImage(file="waks.png")
        w = image6.width()
        h = image6.height()
        window.geometry("%dx%d+0+0" % (w, h))
        panel6 =Label(pagetwo, image=image6)
        panel6.place(x=0,y=80)

        panel6.image = image6

        image7 = PhotoImage(file="waks.png")
        w = image7.width()
        h = image7.height()
        window.geometry("%dx%d+0+0" % (w, h))
        panel7 =Label(pagethree, image=image7)
        panel7.place(x=0,y=80)

        panel7.image = image7

        image8 = PhotoImage(file="waks.png")
        w = image8.width()
        h = image8.height()
        window.geometry("%dx%d+0+0" % (w, h))
        panel8 =Label(pagefour, image=image8)
        panel8.place(x=0,y=80)

        panel8.image = image8

        image9 = PhotoImage(file="waks.png")
        w = image9.width()
        h = image9.height()
        window.geometry("%dx%d+0+0" % (w, h))
        panel9 =Label(pagefive, image=image9)
        panel9.place(x=0,y=80)

        panel9.image = image9

        image10 = PhotoImage(file="waks.png")
        w = image10.width()
        h = image10.height()
        window.geometry("%dx%d+0+0" % (w, h))
        panel10 =Label(pagesixt, image=image10)
        panel10.place(x=0,y=80)

        panel10.image = image10


        ##inpatient
        frame14=Frame(pageone,bg="maroon",width=1900,height=80)
        frame14.place(x=0,y=0)


        button1=Button(frame14,text="Inpatient",width=13,bg="white",fg="red",font="Times 15 bold",relief="raised")
        button1.place(x=14,y=39)
        button2=Button(frame14,text="Outpatient",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagetwo))
        button2.place(x=179,y=39)
        button3=Button(frame14,text="Bills",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagethree))
        button3.place(x=344,y=39)
        button3=Button(frame14,text="Laboratory",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagefour))
        button3.place(x=509,y=39)
        button3=Button(frame14,text="Immunisation",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagefive))
        button3.place(x=674,y=39)
        button3=Button(frame14,text="Dental",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagesixt))
        button3.place(x=839,y=39)

        label=Label(pageone,text="Patient ID:",width=8,font="Times 16",bg="white",fg="blue")
        label.place(x=146,y=154)
        label=Label(pageone,text="First name:",width=8,font="Times 16",bg="white",fg="blue")
        label.place(x=153,y=194)
        label=Label(pageone,text="Last name:",width=10,font="Times 16",bg="white",fg="blue")
        label.place(x=144,y=234)
        label=Label(pageone,text="Age:",width=10,font="Times 16",bg="white",fg="blue")
        label.place(x=170,y=274)
        label=Label(pageone,text="Weight:",width=10,font="Times 16",bg="white",fg="blue")
        label.place(x=155,y=314)
        label4=Checkbutton(pageone,text="Male",bg ="white",fg="blue",font="Times 15")
        label4.place(x=600,y=154)

        check=Checkbutton(pageone,text="Female",bg ="white",fg="blue",font="Times 15")
        check.place(x=740,y=154)

        label=Label(pageone,text="Marital Status:",width=10,font="Times 16",bg="white",fg="blue")
        label.place(x=550,y=194)
        label=Label(pageone,text="Telephone no.:",width=10,font="Times 16",bg="white",fg="blue")
        label.place(x=550,y=234)
        label=Label(pageone,text="Cell phone:",width=8,font="Times 16",bg="white",fg="blue")
        label.place(x=576,y=274)
        label=Label(pageone,text="Residence:",width=10,font="Times 16",bg="white",fg="blue")
        label.place(x=568,y=314)

        txt1=StringVar()
        txt2=StringVar()
        txt3=StringVar()
        txt4=StringVar()
        txt5=StringVar()
        txt6=StringVar()
        txt7=StringVar()
        txt8=StringVar()
        txt9=StringVar()
        txt40=StringVar()
        txt41=StringVar()
        txt42=StringVar()
        txt43=StringVar()

        entry117=Entry(pageone,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt1)
        entry117.place(x=260,y=154)
        entry127=Entry(pageone,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt2)
        entry127.place(x=260,y=194)
        entry37=Entry(pageone,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt3)
        entry37.place(x=260,y=234)
        entry47=Entry(pageone,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt4)
        entry47.place(x=260,y=274)
        entry57=Entry(pageone,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt5)
        entry57.place(x=260,y=314)
        entry67=Entry(pageone,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt6)
        entry67.place(x=680,y=194)
        entry77=Entry(pageone,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt7)
        entry77.place(x=680,y=234)
        entry87=Entry(pageone,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt8)
        entry87.place(x=680,y=274)
        entry97=Entry(pageone,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt9)
        entry97.place(x=680,y=314)
                
                
        label=Label(pageone,text="Next of kin"+"                ",width=80,font="Times 18 bold",bg="white",fg="blue")
        label.place(x=0,y=354)

        label=Label(pageone,text="First name:",width=12,font="Times 16",bg="white",fg="blue")
        label.place(x=165,y=394)
        label=Label(pageone,text="Last name:",width=12,font="Times 16",bg="white",fg="blue")
        label.place(x=153,y=434)
        label=Label(pageone,text="Phone No:",width=14,font="Times 16",bg="white",fg="blue")
        label.place(x=140,y=474)
        label=Label(pageone,text="Residence:",width=11,font="Times 16",bg="white",fg="blue")
        label.place(x=550,y=394)

        entry107=Entry(pageone,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt40)
        entry107.place(x=313,y=394)
        entry197=Entry(pageone,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt41)
        entry197.place(x=313,y=434)
        entry167=Entry(pageone,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt42)
        entry167.place(x=313,y=474)
        entry137=Entry(pageone,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt43)
        entry137.place(x=680,y=394)


        label=Label(pageone,text="Reason",width=10,font="Times 16 bold",bg="white",fg="blue")
        label.place(x=61,y=506)

        text14=Text(pageone,width=80,height=4,font="Times 16",bg="white",fg="black",relief="ridge",bd=3)
        text14.place(x=60,y=539)

        def run():
            if entry117.get()=="" or entry127.get()=="" or entry37.get()=="" or entry47.get()=="" or entry57.get()=="" or entry67.get()=="" or entry77.get()=="" or entry87.get()=="" or entry97.get()=="" or entry107.get()=="" or entry197.get()=="" or entry167.get()=="" or entry137.get()=="":
                print("Please enter all required details in the fields provided")
                label2= Label(pageone,text="Please enter all required details \nin the fields provided",bg="white",fg="red",font= "Times 13")
                label2.place(x=450,y=434)
            else:
                patntid=txt1.get()
                fstname=txt2.get()
                lstname=txt3.get()
                ag=txt4.get()
                weiht=txt5.get()
                mrstus=txt6.get()
                tel=txt7.get()
                cel=txt8.get()
                resd=txt9.get()
                ntfm=txt40.get()
                ntlm=txt41.get()
                ntphn=txt42.get()
                ntresd=txt43.get()

                entry117.delete(0,END)
                entry127.delete(0,END)
                entry37.delete(0,END)
                entry47.delete(0,END)
                entry57.delete(0,END)
                entry67.delete(0,END)
                entry77.delete(0,END)
                entry87.delete(0,END)
                entry97.delete(0,END)
                entry107.delete(0,END)
                entry197.delete(0,END)
                entry167.delete(0,END)
                entry137.delete(0,END)
                
                slq="INSERT INTO inpatient(patid,fname,lname,age,weight,mstatus,telno,celno,resdnce,nxtfname,nxtlname,nxtphneno,nxtresdnce) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)"
                c.execute(slq,(patntid,fstname,lstname,ag,weiht,mrstus,tel,cel,resd,ntfm,ntlm,ntphn,ntresd))
                conn.commit()

                
                tkinter.messagebox.showinfo("Success","Your details were successfully \nentered into the database")

        def ruin():
            patntid=txt1.get()
            fstname=txt2.get()
            lstname=txt3.get()
            ag=txt4.get()
            weiht=txt5.get()
            mrstus=txt6.get()
            tel=txt7.get()
            cel=txt8.get()
            resd=txt9.get()
            ntfm=txt40.get()
            ntlm=txt41.get()
            ntphn=txt42.get()
            ntresd=txt43.get()
            
            sql2=("UPDATE inpatient SET fname=?,lname=?,age=?,weight=?,mstatus=?,telno=?,celno=?,resdnce=?,nxtfname=?,nxtlname=?,nxtphneno=?,nxtresdnce=? WHERE patid=?")
            c.execute(sql2,(fstname,lstname,ag,weiht,mrstus,tel,cel,resd,ntfm,ntlm,ntphn,ntresd,patntid))
            conn.commit()
            tkinter.messagebox.askyesno("Warning","Details will be updated")

        def can():
            patntid=txt1.get()
            sw=("DELETE FROM inpatient WHERE patid=?")
            c.execute(sw,(patntid))
            conn.commit()
            tkinter.messagebox.askyesno("Warning","Details will be Deleted")
            

        baton=Button(pageone,text="Save",width=6,font="Times 13 bold",bg="white",fg="maroon",command=run)
        baton.place(x=150,y=650)
        baton=Button(pageone,text="Update",width=6,font="Times 13 bold",bg="white",fg="maroon",command=ruin)
        baton.place(x=450,y=650)
        baton=Button(pageone,text="Delete",width=6,font="Times 13 bold",bg="white",fg="maroon")
        baton.place(x=750,y=650)

        xx=Button(pageone,width=8,text="Log Out",font="Times 12 bold",bg="white",fg="blue",command=lambda:main(frame1))
        xx.place(x=900,y=660)



        ##outpatient

        frame18=Frame(pagetwo,bg="maroon",width=1900,height=80)
        frame18.place(x=0,y=0)


        button1=Button(frame18,text="Inpatient",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pageone))
        button1.place(x=14,y=39)
        button2=Button(frame18,text="Outpatient",width=13,bg="white",fg="red",font="Times 15 bold",relief="raised")
        button2.place(x=179,y=39)
        button3=Button(frame18,text="Bills",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagethree))
        button3.place(x=344,y=39)
        button3=Button(frame18,text="Laboratory",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagefour))
        button3.place(x=509,y=39)
        button3=Button(frame18,text="Immunisation",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagefive))
        button3.place(x=674,y=39)
        button3=Button(frame18,text="Dental",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagesixt))
        button3.place(x=839,y=39)
            
        label=Label(pagetwo,text="Patient ID:",width=8,font="Times 16",bg="white",fg="blue")
        label.place(x=156,y=154)
        label=Label(pagetwo,text="First name:",width=8,font="Times 16",bg="white",fg="blue")
        label.place(x=153,y=194)
        label=Label(pagetwo,text="Last name:",width=10,font="Times 16",bg="white",fg="blue")
        label.place(x=144,y=234)
        label=Label(pagetwo,text="Age:",width=10,font="Times 16",bg="white",fg="blue")
        label.place(x=170,y=274)
        label=Label(pagetwo,text="Weight:",width=10,font="Times 16",bg="white",fg="blue")
        label.place(x=155,y=314)

        label4=Checkbutton(pagetwo,text="Male",bg ="white",fg="blue",font="Times 15")
        label4.place(x=600,y=154)

        check=Checkbutton(pagetwo,text="Female",bg ="white",fg="blue",font="Times 15")
        check.place(x=740,y=154)
        label=Label(pagetwo,text="Marital Status:",width=10,font="Times 16",bg="white",fg="blue")
        label.place(x=550,y=194)
        label=Label(pagetwo,text="Telephone no.:",width=10,font="Times 16",bg="white",fg="blue")
        label.place(x=550,y=234)
        label=Label(pagetwo,text="Cell phone:",width=8,font="Times 16",bg="white",fg="blue")
        label.place(x=576,y=274)
        label=Label(pagetwo,text="Residence:",width=10,font="Times 16",bg="white",fg="blue")
        label.place(x=568,y=314)

        txt11=StringVar()
        txt12=StringVar()
        txt13=StringVar()
        txt14=StringVar()
        txt15=StringVar()
        txt16=StringVar()
        txt17=StringVar()
        txt18=StringVar()
        txt19=StringVar()
        txt20=StringVar()
        txt21=StringVar()
        txt22=StringVar()

        entry199=Entry(pagetwo,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt11)
        entry199.place(x=260,y=154)
        entry229=Entry(pagetwo,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt12)
        entry229.place(x=260,y=194)
        entry39=Entry(pagetwo,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt13)
        entry39.place(x=260,y=234)
        entry49=Entry(pagetwo,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt14)
        entry49.place(x=260,y=274)
        entry59=Entry(pagetwo,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt15)
        entry59.place(x=260,y=314)
        entry79=Entry(pagetwo,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt16)
        entry79.place(x=680,y=194)
        entry89=Entry(pagetwo,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt17)
        entry89.place(x=680,y=234)
        entry99=Entry(pagetwo,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt18)
        entry99.place(x=680,y=274)
        entry109=Entry(pagetwo,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt19)
        entry109.place(x=680,y=314)
                
                
        label=Label(pagetwo,text="Appointment Details",width=80,font="Times 18 bold",bg="white",fg="blue")
        label.place(x=2,y=354)

        label=Label(pagetwo,text="Doctor's name:",width=12,font="Times 16",bg="white",fg="blue")
        label.place(x=167,y=394)
        label=Label(pagetwo,text="Appointment date:",width=12,font="Times 16",bg="white",fg="blue")
        label.place(x=153,y=434)
        label=Label(pagetwo,text="Appointment time:",width=14,font="Times 16",bg="white",fg="blue")
        label.place(x=140,y=474)

        entry119=Entry(pagetwo,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt20)
        entry119.place(x=315,y=394)
        entry129=Entry(pagetwo,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt21)
        entry129.place(x=315,y=434)
        entry139=Entry(pagetwo,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txt22)
        entry139.place(x=315,y=474)

        label=Label(pagetwo,text="Reason",width=10,font="Times 16 bold",bg="white",fg="blue")
        label.place(x=62,y=506)

        text1=Text(pagetwo,width=80,height=4,font="Times 16",bg="white",fg="black",relief="ridge",bd=3)
        text1.place(x=60,y=539)

        def respond6():
            if entry199.get()=="" or entry229.get()=="" or entry39.get()=="" or entry49.get()=="" or entry59.get()=="" or entry79.get()=="" or entry89.get()=="" or entry99.get()=="" or entry109.get()=="" or entry119.get()=="" or entry129.get()=="" or entry139.get()=="":
                print("Please enter all required details in the fields provided")
                label2= Label(pagetwo,text="Please enter all required details \nin the fields provided",bg="white",fg="red",font= "Times 13")
                label2.place(x=620,y=424)
            else:
                pat=txt11.get()
                fnem=txt12.get()
                lnem=txt13.get()
                aga=txt14.get()
                wait=txt15.get()
                mstus=txt16.get()
                teln=txt17.get()
                celn=txt18.get()
                resd=txt19.get()
                doctn=txt20.get()
                appd=txt21.get()
                appt=txt22.get()

                entry199.delete(0,END)
                entry229.delete(0,END)
                entry39.delete(0,END)
                entry49.delete(0,END)
                entry59.delete(0,END)
                entry79.delete(0,END)
                entry89.delete(0,END)
                entry99.delete(0,END)
                entry109.delete(0,END)
                entry119.delete(0,END)
                entry129.delete(0,END)
                entry139.delete(0,END)

                sq2="INSERT INTO Outpatient(patid,fname,lname,age,weight,mstatus,telno,celno,resdnce,doctorsname,appdate,apptime) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"
                c.execute(sq2,(pat,fnem,lnem,aga,wait,mstus,teln,celn,resd,doctn,appd,appt))
                conn.commit()
                
                tkinter.messagebox.showinfo("Success","Your details were successfully \nentered into the database")

        def raw3():
            pat=txt11.get()
            fnem=txt12.get()
            lnem=txt13.get()
            aga=txt14.get()
            wait=txt15.get()
            mstus=txt16.get()
            teln=txt17.get()
            celn=txt18.get()
            resd=txt19.get()
            doctn=txt20.get()
            appd=txt21.get()
            appt=txt22.get()
            
            sql2=("UPDATE Outpatient SET fname=?,lname=?,age=?,weight=?,mstatus=?,telno=?,celno=?,resdnce=?,doctorsname=?,appdate=?,apptime=? WHERE patid=?")
            c.execute(sql2,(fnem,lnem,aga,wait,mstus,teln,celn,resd,doctn,appd,appt,pat))
            conn.commit()
            tkinter.messagebox.askyesno("Warning","Details will be updated")


        def can():
            patntid=txt1.get()
            sw=("DELETE FROM Outpatient WHERE patid=?")
            c.execute(sw,[(pat)])
            conn.commit()
            tkinter.messagebox.askyesno("Warning","Details will be Deleted")

        baton=Button(pagetwo,text="Save",width=6,font="Times 13 bold",bg="white",fg="maroon",command=respond6)
        baton.place(x=150,y=650)
        baton=Button(pagetwo,text="Update",width=6,font="Times 13 bold",bg="white",fg="maroon",command=raw3)
        baton.place(x=450,y=650)
        baton=Button(pagetwo,text="Delete",width=6,font="Times 13 bold",bg="white",fg="maroon",command=can)
        baton.place(x=750,y=650)
        
        xx=Button(pagetwo,width=8,text="Log Out",font="Times 12 bold",bg="white",fg="blue",command=lambda:main(frame1))
        xx.place(x=900,y=660)



        ##Bills
        frame14=Frame(pagethree,bg="maroon",width=1900,height=80)
        frame14.place(x=0,y=0)


        button1=Button(frame14,text="Inpatient",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pageone))
        button1.place(x=14,y=39)
        button2=Button(frame14,text="Outpatient",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagetwo))
        button2.place(x=179,y=39)
        button3=Button(frame14,text="Bills",width=13,bg="white",fg="red",font="Times 15 bold",relief="raised")
        button3.place(x=344,y=39)
        button3=Button(frame14,text="Laboratory",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagefour))
        button3.place(x=509,y=39)
        button3=Button(frame14,text="Immunisation",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagefive))
        button3.place(x=674,y=39)
        button3=Button(frame14,text="Dental",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagesixt))
        button3.place(x=839,y=39)


        label=Label(pagethree,text="Patient ID:",width=8,font="Times 16",bg="white",fg="blue")
        label.place(x=156,y=154)
        label=Label(pagethree,text="Consultation Fee:",width=14,font="Times 16",bg="white",fg="blue")
        label.place(x=92,y=194)
        label=Label(pagethree,text="Medical Fee:",width=10,font="Times 16",bg="white",fg="blue")
        label.place(x=135,y=234)
        label=Label(pagethree,text="Current Pay:",width=10,font="Times 16",bg="white",fg="blue")
        label.place(x=135,y=274)
        label=Label(pagethree,text="Balance:",width=10,font="Times 16",bg="white",fg="blue")
        label.place(x=150,y=314)

        label=Label(pagethree,text="Received by:",width=10,font="Times 16",bg="white",fg="blue")
        label.place(x=550,y=194)
        label=Label(pagethree,text="Total:",width=10,font="Times 16",bg="white",fg="blue")
        label.place(x=163,y=360)
        label=Label(pagethree,text="Date of payment:",width=15,font="Times 16",bg="white",fg="blue")
        label.place(x=85,y=410)

        tx10=StringVar()
        tx11=StringVar()
        tx12=StringVar()
        tx13=StringVar()
        tx14=StringVar()
        tx15=StringVar()
        tx16=StringVar()
        tx17=StringVar()

        entr167=Entry(pagethree,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tx10)
        entr167.place(x=260,y=154)
        entr269=Entry(pagethree,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tx11)
        entr269.place(x=260,y=194)
        entr367=Entry(pagethree,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tx12)
        entr367.place(x=260,y=234)
        entr467=Entry(pagethree,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tx13)
        entr467.place(x=260,y=274)
        entr567=Entry(pagethree,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tx14)
        entr567.place(x=260,y=314)
        entr667=Entry(pagethree,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tx15)
        entr667.place(x=260,y=360)
        entr767=Entry(pagethree,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tx16)
        entr767.place(x=680,y=194)
        entr867=Entry(pagethree,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=tx17)
        entr867.place(x=260,y=410)


        label=Label(pagethree,text="Add note",width=10,font="Times 16 bold",bg="white",fg="blue")
        label.place(x=62,y=475)

        text1=Text(pagethree,width=80,height=5,font="Times 16",bg="white",fg="black",relief="ridge",bd=3)
        text1.place(x=60,y=505)

        def rep6():
            if entr167.get()=="" or entr269.get()=="" or entr367.get()=="" or entr467.get()=="" or entr567.get()=="" or entr667.get()=="" or entr767.get()=="" or entr867.get()=="":
                print("Please enter all required details in the fields provided")
                label2= Label(pagethree,text="Please enter all required details \nin the fields provided",bg="white",fg="red",font= "Times 13")
                label2.place(x=590,y=424)
            else:
                patd=tx10.get()
                cfee=tx11.get()
                mdfee=tx12.get()
                cntfee=tx13.get()
                balnce=tx14.get()
                recvdby=tx15.get()
                total=tx16.get()
                dateofpmt=tx17.get()

                entr167.delete(0,END)
                entr269.delete(0,END)
                entr367.delete(0,END)
                entr467.delete(0,END)
                entr567.delete(0,END)
                entr667.delete(0,END)
                entr767.delete(0,END)
                entr867.delete(0,END)

                sqz="INSERT INTO Bills(patid,consutnfee,medicfee,currentpay,balance,total,dofpyment,receivedby) VALUES(?,?,?,?,?,?,?,?)"
                c.execute(sqz,(patd,cfee,mdfee,cntfee,balnce,recvdby,total,dateofpmt))
                conn.commit()
                
                tkinter.messagebox.showinfo("Success","Your details were successfully \nentered into the database")

        def can():
            patntid=txt1.get()
            sw=("DELETE FROM Bills WHERE patid=?")
            c.execute(sw,[(patd)])
            conn.commit()
            tkinter.messagebox.askyesno("Warning","Details will be Deleted")


        button=Button(pagethree,text="Save",width=8,font="Times 13 bold",bg="white",fg="maroon",command=rep6)
        button.place(x=150,y=650)
        baton=Button(pagethree,text="Update",width=6,font="Times 13 bold",bg="white",fg="maroon")
        baton.place(x=450,y=650)
        baton=Button(pagethree,text="Delete",width=6,font="Times 13 bold",bg="white",fg="maroon",command=can)
        baton.place(x=750,y=650)
        
        xx=Button(pagethree,width=8,text="Log Out",font="Times 12 bold",bg="white",fg="blue",command=lambda:main(frame1))
        xx.place(x=900,y=660)



        ##Laboratory
        frame19=Frame(pagefour,bg="light blue",width=1900,height=80)
        frame19.place(x=0,y=0)

        button1=Button(frame19,text="Inpatient",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pageone))
        button1.place(x=14,y=39)
        button2=Button(frame19,text="Outpatient",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagetwo))
        button2.place(x=179,y=39)
        button3=Button(frame19,text="Bills",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagethree))
        button3.place(x=344,y=39)
        button3=Button(frame19,text="Laboratory",width=13,bg="white",fg="red",font="Times 15 bold",relief="raised")
        button3.place(x=509,y=39)
        button3=Button(frame19,text="Immunisation",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagefive))
        button3.place(x=674,y=39)
        button3=Button(frame19,text="Dental",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagesixt))
        button3.place(x=839,y=39)
        
        label=Label(pagefour,text="Names:",width=9,font="Times 16",bg="white",fg="blue")
        label.place(x=246,y=154)
        label=Label(pagefour,text="Age:",width=8,font="Times 16",bg="white",fg="blue")
        label.place(x=243,y=214)
        label=Label(pagefour,text="Address:",width=10,font="Times 16",bg="white",fg="blue")
        label.place(x=234,y=334)
        label=Label(pagefour,text="Test Results:",width=10,font="Times 16",bg="white",fg="blue")
        label.place(x=234,y=360)

        label4=Checkbutton(pagefour,text="Inpatient",bg ="white",fg="blue",font="Times 14 bold")
        label4.place(x=250,y=274)
        check=Checkbutton(pagefour,text="Outpatient",bg ="white",fg="blue",font="Times 14 bold")
        check.place(x=440,y=274)


        label=Label(pagefour,text="Clinical Notes",width=10,font="Times 16 bold",bg="white",fg="blue")
        label.place(x=62,y=414)

        text1=Text(pagefour,width=80,height=8,font="Times 16",bg="white",fg="black",relief="ridge",bd=3)
        text1.place(x=60,y=440)

        txe10=StringVar()
        txe11=StringVar()
        txe12=StringVar()
        txe13=StringVar()

        entry478=Entry(pagefour,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txe10)
        entry478.place(x=405,y=154)
        entry578=Entry(pagefour,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txe11)
        entry578.place(x=405,y=214)
        entry678=Entry(pagefour,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txe12)
        entry678.place(x=405,y=334)
        entry778=Entry(pagefour,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txe13)
        entry778.place(x=405,y=360)
        def response():
            if entry478.get()=="" or entry578.get()=="" or entry678.get()==""or entry778.get()=="":
                print("Please enter all required details in the fields provided")
                label2= Label(pagefour,text="Please enter all required details in the fields provided",bg="white",fg="red",font= "Times 13")
                label2.place(x=320,y=380)
            else:
                wakaid=txe10.get()
                patid=txe11.get()
                testr=txe12.get()
                tests=txe13.get()

                entry478.delete(0,END)
                entry578.delete(0,END)
                entry678.delete(0,END)
                entry778.delete(0,END)

                sqa="INSERT INTO Labs(names,age,address,tests) VALUES(?,?,?,?)"
                c.execute(sqa,(wakaid,patid,testr,tests))
                conn.commit()
                
                tkinter.messagebox.showinfo("Success","Your details were successfully \nentered into the database")

        def can():
            patntid=txt1.get()
            sw=("DELETE FROM Labs WHERE names=?")
            c.execute(sw,[(patid)])
            conn.commit()
            tkinter.messagebox.askyesno("Warning","Details will be Deleted")
            
        baton=Button(pagefour,text="Save",width=6,font="Times 13 bold",bg="white",fg="maroon",command=response,relief="raised")
        baton.place(x=150,y=650)
        baton=Button(pagefour,text="Update",width=6,font="Times 13 bold",bg="white",fg="maroon")
        baton.place(x=450,y=650)
        baton=Button(pagefour,text="Delete",width=6,font="Times 13 bold",bg="white",fg="maroon",command=can)
        baton.place(x=750,y=650)
        
        xx=Button(pagefour,width=8,text="Log Out",font="Times 12 bold",bg="white",fg="blue",command=lambda:main(frame1))
        xx.place(x=900,y=660)


        ##Immunisation
        frame16=Frame(pagefive,bg="light blue",width=1900,height=80)
        frame16.place(x=0,y=0)

        button1=Button(frame16,text="Inpatient",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pageone))
        button1.place(x=14,y=39)
        button2=Button(frame16,text="Outpatient",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagetwo))
        button2.place(x=179,y=39)
        button3=Button(frame16,text="Bills",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagethree))
        button3.place(x=344,y=39)
        button3=Button(frame16,text="Laboratory",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagefour))
        button3.place(x=509,y=39)
        button3=Button(frame16,text="Immunisation",width=13,bg="white",fg="red",font="Times 15 bold",relief="raised")
        button3.place(x=674,y=39)
        button3=Button(frame16,text="Dental",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagesixt))
        button3.place(x=839,y=39)
        

        def rund4():
            try:
                if entryr.get()=="":
                    lablezs=Label(pagefive,text="Please fill in the space provided ????",fg="red",font="Times 14",bg="white")
                    lablezs.place(x=280,y=118)
                    print("Please fill in the space provided ????")
                else:
                    frameba=Frame(window,width=2200,height=740)
                    frameba.grid(row=0,column=0,sticky="news")
                    sqba=("SELECT * FROM Immune WHERE patientid=?")
                    c.execute(sqba,([entryr.get()]))
                    rowsz =c.fetchall()
                    for roxyv in rowsz:
                        print(roxyv)
                       
                    baton=Button(frameba,text="Back",fg="white",bg="blue",font="Times 14",command=lambda:remain(pagefive))
                    baton.place(x=20,y=10)
                    text90=Text(frameba,width=123,height=50,bg="white")
                    text90.place(x=15,y=70)
                    text90.insert(INSERT,roxyv)
            except UnboundLocalError:
                lablezd=Label(frameba,text="We are sorry\nWe don't have such records here!!!",fg="red",font="Times 15",bg="white")
                lablezd.place(x=340,y=118)
                print("No Such records")


        label=Label(pagefive,text="Patient Name:",width=9,font="Times 16",bg="white",fg="blue")
        label.place(x=246,y=154)
        label=Label(pagefive,text="Age",width=8,font="Times 16",bg="white",fg="blue")
        label.place(x=243,y=214)
        label=Label(pagefive,text="Parent name:",width=15,font="Times 16",bg="white",fg="blue")
        label.place(x=234,y=334)
        label=Label(pagefive,text="Address:",width=13,font="Times 16",bg="white",fg="blue")
        label.place(x=640,y=154)
        label=Label(pagefive,text="Immunisation Against:",width=13,font="Times 16",bg="white",fg="blue")
        label.place(x=640,y=214)

        label4=Checkbutton(pagefive,text="Inpatient",bg ="white",fg="blue",font="Times 14 bold")
        label4.place(x=250,y=274)

        check=Checkbutton(pagefive,text="Outpatient",bg ="white",fg="blue",font="Times 14 bold")
        check.place(x=440,y=274)


        label=Label(pagefive,text="Clinical Notes",width=10,font="Times 16 bold",bg="white",fg="blue")
        label.place(x=62,y=414)

        text1=Text(pagefive,width=80,height=8,font="Times 16",bg="white",fg="black",relief="ridge",bd=3)
        text1.place(x=60,y=440)

        txet10=StringVar()
        txet11=StringVar()
        txet12=StringVar()
        txet13=StringVar()
        txet14=StringVar()
                    

        entry654=Entry(pagefive,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txet10)
        entry654.place(x=405,y=154)
        entry754=Entry(pagefive,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txet11)
        entry754.place(x=405,y=214)
        entry854=Entry(pagefive,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txet12)
        entry854.place(x=420,y=334)
        entry954=Entry(pagefive,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txet13)
        entry954.place(x=790,y=154)
        entry9554=Entry(pagefive,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txet14)
        entry9554.place(x=790,y=214)
        def response():
            if entry654.get()=="" or entry754.get()=="" or entry854.get()=="" or entry954.get()==""or entry9554.get()=="":
                print("Please enter all required details in the fields provided")
                label2= Label(pagefive,text="Please enter all required details in the fields provided",bg="white",fg="red",font= "Times 13")
                label2.place(x=410,y=380)
            else:
                wakid=txet10.get()
                patid=txet11.get()
                immagnst=txet12.get()
                doctaz=txet13.get()
                fsd=txet14.get()

                entry654.delete(0,END)
                entry754.delete(0,END)
                entry854.delete(0,END)
                entry954.delete(0,END)
                entry9554.delete(0,END)

                sqd="INSERT INTO Immune(Patientname,Age,Parentname,Address,disease) VALUES(?,?,?,?,?)"
                c.execute(sqd,(wakid,patid,immagnst,doctaz,fsd))
                
                conn.commit()
                tkinter.messagebox.showinfo("Success","Your details were successfully \nentered into the database")

        def can():
            patntid=txt1.get()
            sw=("DELETE FROM Immune WHERE patientname=?")
            c.execute(sw,[(patid)])
            conn.commit()
            tkinter.messagebox.askyesno("Warning","Details will be Deleted")
            
            
        baton=Button(pagefive,text="Save",width=6,font="Times 13 bold",bg="white",fg="maroon",command=response,relief="raised")
        baton.place(x=150,y=650)
        baton=Button(pagefive,text="Update",width=6,font="Times 13 bold",bg="white",fg="maroon")
        baton.place(x=450,y=650)
        baton=Button(pagefive,text="Delete",width=6,font="Times 13 bold",bg="white",fg="maroon",command=can)
        baton.place(x=750,y=650)
        
        xx=Button(pagefive,width=8,text="Log Out",font="Times 12 bold",bg="white",fg="blue",command=lambda:main(frame1))
        xx.place(x=900,y=660)

        ##Dental

        frame16=Frame(pagesixt,bg="maroon",width=1900,height=80)
        frame16.place(x=0,y=0)

        button1=Button(frame16,text="Inpatient",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pageone))
        button1.place(x=14,y=39)
        button2=Button(frame16,text="Outpatient",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagetwo))
        button2.place(x=179,y=39)
        button3=Button(frame16,text="Bills",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagethree))
        button3.place(x=344,y=39)
        button3=Button(frame16,text="Laboratory",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagefour))
        button3.place(x=509,y=39)
        button3=Button(frame16,text="Immunisation",width=13,bg="white",fg="green",font="Times 15 bold",relief="raised",command=lambda:remain(pagefive))
        button3.place(x=674,y=39)
        button3=Button(frame16,text="Dental",width=13,bg="white",fg="red",font="Times 15 bold",relief="raised")
        button3.place(x=839,y=39)
        

        label=Label(pagesixt,text="Worker's ID:",width=9,font="Times 16",bg="white",fg="blue")
        label.place(x=246,y=154)
        label=Label(pagesixt,text="Patient ID:",width=8,font="Times 16",bg="white",fg="blue")
        label.place(x=243,y=214)
        label=Label(pagesixt,text="Lab Technician:",width=15,font="Times 16",bg="white",fg="blue")
        label.place(x=234,y=334)

        label4=Checkbutton(pagesixt,text="Inpatient",bg ="white",fg="blue",font="Times 14 bold")
        label4.place(x=250,y=274)

        check=Checkbutton(pagesixt,text="Outpatient",bg ="white",fg="blue",font="Times 14 bold")
        check.place(x=440,y=274)


        label=Label(pagesixt,text="Clinical Notes",width=10,font="Times 16 bold",bg="white",fg="blue")
        label.place(x=62,y=414)

        text1=Text(pagesixt,width=80,height=8,font="Times 16",bg="white",relief="ridge",bd=3)
        text1.place(x=60,y=440)

        txeta10=StringVar()
        txeta11=StringVar()
        txeta12=StringVar()
        

        entry1023=Entry(pagesixt,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txeta10)
        entry1023.place(x=405,y=154)
        entry1123=Entry(pagesixt,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txeta11)
        entry1123.place(x=405,y=214)
        entry1223=Entry(pagesixt,width=17,font="Times 15",bg="white",fg="black",relief="ridge",bd=3,textvariable=txeta12)
        entry1223.place(x=405,y=334)
        def response():
            if entry1023.get()=="" or entry1123.get()=="" or entry1223.get()=="":
                print("Please enter all required details in the fields provided")
                label2= Label(pagesixt,text="Please enter all required details in the fields provided",bg="white",fg="red",font= "Times 13")
                label2.place(x=320,y=390)
            else:
                wakid=txeta10.get()
                patd=txeta11.get()
                labtec=txeta12.get()

                entry1023.delete(0,END)
                entry1123.delete(0,END)
                entry1223.delete(0,END)
                
                sqf="INSERT INTO Dental(workerid,patientid,labtech) VALUES(?,?,?)"
                c.execute(sqf,(wakid,patd,labtec))
                conn.commit()
                
                tkinter.messagebox.showinfo("Success","Your details were successfully \nentered into the database")
            
        baton=Button(pagesixt,text="Save",width=6,font="Times 13 bold",bg="white",fg="maroon",command=response,relief="raised")
        baton.place(x=150,y=650)
        baton=Button(pagesixt,text="Update",width=6,font="Times 13 bold",bg="white",fg="maroon")
        baton.place(x=450,y=650)
        baton=Button(pagesixt,text="Delete",width=6,font="Times 13 bold",bg="white",fg="maroon")
        baton.place(x=750,y=650)
        
        xx=Button(pagesixt,width=8,text="Log Out",font="Times 12 bold",bg="white",fg="blue",command=lambda:main(frame1))
        xx.place(x=900,y=660)
        
        
        remain(pageone)


    elif userid=="" or paswad=="":
        print("Please fill in the space provided")
        label=Label(window,text="Please fill in your details in the space provided ?",fg="red",bg="white",font="Times 14")
        label.place(x=360,y=480)
    else:
        print("Please review either your username or password")
        tkinter.messagebox.showwarning("Warning","Please review either your username or password")

def callback():
        print("Hey")
def respond():
    root=Tk()
    root.geometry("800x500")
    root.configure(bg="grey")
    root.title("Help")
    lab=Label(root,text="Welcome to our Patient Record Management system that is \ngona make record keeping much easier in you hospital or medical facility",fg="red",font="Times 15")
    lab.place(x=20,y=50)
        
button1=Button(frame1,text='Log In',width=22, bg= "white",fg="maroon",relief="raised",font="Times 14 bold",command=reply)
button1.place(x=420,y=412)
message1=Message(frame1,text="Patient Record"+"\nManagement System",font="Times 14 italic",fg="blue")
message1.place(x=600,y=160)



main(frame1)
window.mainloop()
