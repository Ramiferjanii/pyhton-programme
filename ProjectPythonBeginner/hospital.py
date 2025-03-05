from tkinter import*
from tkinter import Button , Frame , Tk , ttk
import random 
import time 
import datetime
from tkinter import messagebox 
import mysql.connector

class hospital : 
    def __init__(self,root):
        self.root = root 
        self.root.title(" Hospital Managment system ")
        self.root.geometry("1540x800+0+0")

        self.nameoftables=StringVar()
        self.ref=StringVar()
        self.does=StringVar()
        self.numbersoftables=StringVar()
        self.lot=StringVar()
        self.issuesdate=StringVar()
        self.expdate=StringVar()
        self.dailydose=StringVar()
        self.sideeeffect=StringVar()
        self.furtherinformation=StringVar()
        self.storageadvice=StringVar()
        self.drivingusingmedication=StringVar()
        self.howtousemedication=StringVar()
        self.patientid=StringVar()
        self.nhsnumbers=StringVar()
        self.patientname=StringVar()
        self.dateofbirth=StringVar()
        self.patientadresse=StringVar()

        lbltitle=Label(self.root ,bd = 20 , relief = RIDGE , text = "HOSPITAL MANAGMENT SYSTEM " , fg = "red" , bg="white" , font=("times new roman" ,50 , "bold" ) )
        lbltitle.pack(side=TOP , fill = X )



        # ===================================== dataframe =====================================
        dataframe=Frame(self.root , bd=20 , relief=RIDGE )
        dataframe.place ( x=0 , y=130 , width=1530 , height=400 )

        dataframeleft =LabelFrame(dataframe , bd=10 , relief= RIDGE , padx=10
                                                                        , font=("arial" ,12 , "bold" )  , text= " Patient Information" ) 
        dataframeleft.place(x=0 , y=5 , width=900 , height= 350  ) 


        dataframeright =LabelFrame(dataframe , bd=10 , relief= RIDGE , padx=10
                                                                        , font=("times new roman" ,12 , "bold" )  , text= "Prescription" ) 
        dataframeright.place(x=990 , y=5 , width=460 , height= 350  ) 


        # ================================= buttom frame ====================================
        buttonframe=Frame(self.root , bd=20 , relief=RIDGE )
        
        buttonframe.place ( x=0 , y=530 , width=1530 , height=70 )
        # ================================= buttom frame ====================================
        detailsframe=Frame(self.root , bd=20 , relief=RIDGE )
        detailsframe.place ( x=0 , y=600 , width=1530 , height=190 )
        
        
        # =================================Data frame left====================================
        lblnametable= Label(dataframeleft , text="Names OF Tablet" , font=("arial" , 12 , "bold") , padx= 2 ,pady= 6)
        lblnametable.grid(row= 0  , column= 0 ,sticky=W) 

        comenametablet= ttk.Combobox(dataframeleft ,textvariable=self.nameoftables ,state="readonly" ,  font=("arial" , 12 , "bold") , width= 33)
        comenametablet["values"] = ("Nice" , "corona vacine " , "Acetaminophen" , "Adderall" , "Amlodipine" , "Ativen" )
        comenametablet.current(0)
        comenametablet.grid (row=0 , column= 1)
        lblref = Label (dataframeleft , font= ("arial" , 12 , "bold" ) , text= "Refence No : " , padx= 2) 
        lblref.grid(row=1 , column= 0  , sticky= W )
        txtref = Entry (dataframeleft , font= ("arial" , 13 , "bold") , width= 35) 
        txtref.grid (row= 1 , column= 1 )


        lbldose = Label(dataframeleft , font= ("arial" , 12 , "bold" ) , text="Dose : " , padx= 2 , pady= 4) 
        lbldose.grid(row=2 , column= 0 , sticky=W) 
        txtdose = Entry (dataframeleft , font= ("arial" , 13 , "bold" ) , width= 30)
        txtdose.grid(row= 2 , column= 1) 

        lblnooftablets = Label (dataframeleft , font=("arial" , 12 , " bold") ,text="NO  OF Tablets :" , padx= 2 , pady= 6)
        lblnooftablets.grid (row= 3 , column=0 , sticky= W)
        txtnooftablets = Entry (dataframeleft , font= ("arial" , 13 , "bold" ) , width= 30) 
        txtnooftablets.grid(row= 3 , column=1)
        


        lbllot = Label(dataframeleft , font=("arial" , 12 , "bold") , text= "LOT :" , padx= 2 , pady= 6 ) 
        lbllot.grid (row=4 , column= 0 , sticky= W)
        txtlot = Entry (dataframeleft , font= ("arial", 13 , "bold"  ) , width= 30  )
        txtlot.grid(row= 4 , column= 1 )

        lblissuedate = Label(dataframeleft , font= ("arial" , 12 , "bold") , text= "Issue date :" , padx= 2 , pady= 6  ) 
        lblissuedate.grid (row= 5 , column= 0 , sticky= W)
        textissuedate = Entry (dataframeleft , font= ("arial" , 13 , "bold") , width= 30)
        textissuedate.grid (row=5 , column= 1 )


        lblexpdate = Label (dataframeleft , font= ("arial" , 12 , "bold") ,text="Exp Date : " ,padx= 1 , pady= 5)
        lblexpdate.grid(row=6 , column= 0 ,sticky= W)
        txtexpdate = Entry (dataframeleft , font= ("arial" , 13 , "bold" ) ,width= 30)
        txtexpdate.grid (row=6 , column= 1 )


        lbldailydose = Label (dataframeleft , font= ("arial" , 12 , "bold") , text= "Daily Dose : " , padx= 2 , pady=4)
        lbldailydose.grid(row= 7 , column=0 ,  sticky= W )
        txtdailydose = Entry (dataframeleft , font= ("arial" , 13 , "bold" ) , width= 30)
        txtdailydose.grid (row=7 , column= 1 )

        lblsideeffect = Label (dataframeleft , font= ("arial" , 12 , "bold") , text= "Side Effect : " , padx= 2  , pady= 6)
        lblsideeffect.grid(row=8 , column= 0 , sticky= W )
        txtsideeffect = Entry (dataframeleft , font= ("arial", 13 , "bold") , width= 30)
        txtsideeffect.grid(row=8 , column=1)

        lblfurtherinfo = Label (dataframeleft , font= ("arial", 12 , "bold") ,text= "Further Information :" , padx= 2)
        lblfurtherinfo.grid(row=0 , column= 2 , sticky= W )
        txtfurtherinfo = Entry (dataframeleft , font= ("arial" , 13 , "bold") , width= 30)
        txtfurtherinfo.grid (row=0 , column=3) 


        lblbloodpressure = Label (dataframeleft , font= ("arial" , 12 , "bold") , text= "Blood Pressure : " , padx= 2 , pady= 6)
        lblbloodpressure.grid(row=1 , column=2 , sticky= W)
        txtbloodpressure = Entry (dataframeleft , font= ("arial", 13 , "bold") , width= 30)
        txtbloodpressure.grid(row=1 , column=3)


        lblstorage = Label (dataframeleft , font=("arial" , 12 , "bold") , text= "Storage Advice :" , padx= 2 , pady=6)
        lblstorage.grid (row= 2 , column=2  ,  sticky= W )
        txtstorage = Entry (dataframeleft , font= ("arial" , 13 , "bold" ) , width= 30)
        txtstorage.grid (row= 2 , column= 3)



        lblmedicine = Label (dataframeleft , font= ("arial", 12 , "bold") , text= "Medication : " , padx= 2 , pady=6)
        lblmedicine.grid (row=3  , column= 2 , sticky= W )
        txtmedicine = Entry (dataframeleft , font= ("arial" , 13 , "bold") , width=30 )
        txtmedicine.grid (row=3 , column=3)

        lblpatientid = Label (dataframeleft , font= ( "arial" , 12 , " bold" ) ,  text= "Patient ID :" , padx= 2 , pady= 6)
        lblpatientid.grid(row=4 , column=2 , sticky= W )
        txtpatientid = Entry (dataframeleft , font= ( "arial" , 13 , "bold") , width= 30)
        txtpatientid.grid( row=4 , column= 3)


        lblnhsnumber = Label (dataframeleft , font= ("arial" , 12 , "bold" ) , text= "NHS Number :" , padx= 2 , pady=6)
        lblnhsnumber.grid(row = 5 , column= 2 , sticky= W )
        txtnhsnumber = Entry ( dataframeleft , font= ( "arial" , 13 , "bold") , width= 30)
        txtnhsnumber.grid ( row= 5 , column= 3)


        lblpatientname = Label ( dataframeleft , font= ("arial" , 12 , "bold") , text= "Patient Name :" , padx= 2 , pady= 6)
        lblpatientname.grid (row= 6 , column=2 , sticky= W )
        txtpatientname = Entry (dataframeleft , font= ( "arial" , 13 , "bold") , width= 30)
        txtpatientname.grid(row=6 , column=3 )


        lblbirth = Label ( dataframeleft , font= ( "arial" , 12 , "bold") , text= "Date OF Birth :" , padx= 2 , pady=6)
        lblbirth.grid (row=7 , column= 2 , sticky= W )
        txtbirth = Entry (dataframeleft , font= ("arial", 13 , "bold") , width= 30)
        txtbirth.grid(row=7 , column= 3 )


        lbladresse = Label ( dataframeleft , font= ("arial" , 12 , "bold") , text= "Patient Adresse :" , padx= 2 , pady=6 )
        lbladresse.grid(row=8 , column= 2 , sticky= W )
        txtadresse = Entry (dataframeleft , font= ("arial" , 13 , "bold") , width= 30)
        txtadresse.grid ( row= 8 , column= 3 )









        # ========================================== DATA FRAME RIGHT ===================================
        self.txtprescription= Text(dataframeright , font= ("arial" , 12 , "bold") , width= 45 , height= 16 , padx= 2 , pady= 6 )
        self.txtprescription.grid (row= 0 , column= 0)



        # ==============================================  buttom ===================================================
        btnprescription = Button(buttonframe, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"), width=23, height=16, padx=2, pady=6)
        btnprescription.grid(row=0, column=0)

        btnprescriptiondata=   Button ( buttonframe ,  text= "Prescription  DATA", bg= "green"  , fg="white" ,   font= ("arial" , 12 , "bold") , width= 23 , height= 16 , padx= 2 , pady= 6 )
        btnprescriptiondata.grid (row= 0 , column= 1 )




        btnupdate=   Button ( buttonframe ,  text= "UPDATE", bg="green"  , fg="white" ,   font= ("arial" , 12 , "bold") , width= 23 , height= 16 , padx= 2 , pady= 6 )
        btnupdate.grid (row= 0 , column= 2 )




        btndelete=   Button ( buttonframe ,  text= "DELETE", bg="green"  , fg="white" ,   font= ("arial" , 12 , "bold") , width= 23 , height= 16 , padx= 2 , pady= 6 )
        btndelete.grid (row= 0 , column= 3 )



        btnclear=   Button ( buttonframe ,  text= "CLEAR", bg="green"  , fg="white" ,   font= ("arial" , 12 , "bold") , width= 23 , height= 16 , padx= 2 , pady= 6 )
        btnclear.grid (row= 0 , column= 4 )

        btnexit=   Button ( buttonframe ,  text= "EXIT", bg="green"  , fg="white" ,   font= ("arial" , 12 , "bold") , width= 23 , height= 16 , padx= 2 , pady= 6 )
        btnexit.grid (row= 0 , column= 5 )



        #============================================= table ================================================================
        # ======================================== scollbar =====================================================================


        scroll_x = ttk.Scrollbar(detailsframe , orient= HORIZONTAL)
        scroll_y = ttk.Scrollbar(detailsframe , orient= VERTICAL)
        self.hospital_table = ttk.Treeview (detailsframe , columns=( "nameoftable" , "ref" , "dose" , "nooftablets" , "lot", "issuedate" ,
                                                                    "dailysoes" , "expdate" , "storage" , "nhsnumber" , "pname" , "dob" , "adresse") , yscrollcommand = scroll_y.set , xscrollcommand = scroll_x.set ) 
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x = ttk.Scrollbar(command= self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command= self.hospital_table.yview)

        self.hospital_table.heading("nameoftable" , text= "Name OF Tables"  )
        self.hospital_table.heading("ref" , text= "Reference NO."  )
        self.hospital_table.heading("dose" , text= "Dose"  )
        self.hospital_table.heading("nooftablets" , text= "No Of Tbales "  )
        self.hospital_table.heading("lot" , text= "LOT"  )
        self.hospital_table.heading("issuedate" , text= "Issue Date"  )
        self.hospital_table.heading("expdate" , text= "Exp Date"  )
        self.hospital_table.heading("dailysoes" , text= "Daily Dates"  )
        self.hospital_table.heading("storage" , text= "Storage"  )
        self.hospital_table.heading("nhsnumber" , text= "NHS Numbers"  )
        self.hospital_table.heading("pname" , text= "Patient Name"  )
        self.hospital_table.heading("dob" , text= "DOB"  )
        self.hospital_table.heading("adresse" , text= "Adresse"  )
        self.hospital_table["show"] = "headings"


        self.hospital_table.pack(fill=BOTH , expand=1)













        #=========================== functionality declaration===================================

    def iprescriptiondata (self) :
        if self.nameoftables.get() =="" or self.ref.get() == "" :
            messagebox.showerror("error" , " All fields are required")
        else : 
            conn=mysql.connector.connect(host="localhost" , username = "root" , password="14603779" , database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,) " ,(
                                                                                self.nameoftables.get ,
                                                                                self.ref.get ,
                                                                                self.does.get ,
                                                                                self.numbersoftables.get ,
                                                                                self.does.get ,
                                                                                self.lot.get ,
                                                                                self.issuesdate.get ,
                                                                                self.expdate.get ,
                                                                                self.dailydose.get ,
                                                                                self.storageadvice.get ,
                                                                                self.nhsnumbers.get ,
                                                                                self.patientname.get ,
                                                                                self.dateofbirth.get ,
                                                                                self.patientadresse.get ,
                                                                                ) )
            conn.commit()
            conn.close()


    def fatch_











        











root = Tk()

ob=hospital(root)
root.mainloop()




