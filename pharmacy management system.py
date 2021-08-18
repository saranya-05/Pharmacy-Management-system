import sqlite3
from sqlite3 import Error
import time
import sys
import os
cls = lambda: os.system('cls')
con = sqlite3.connect('pharmacy.db')
cur = con.cursor()

                     #creating tables
def pharmacy(con):
    cur.execute("create table pharmacy(phar_id integer(5) primary key,name varchar(20),address varchar(20))")
    con.commit()
    
def drug(con):
    cur.execute("create table drug(drug_id integer(5) primary key,name varchar(20),generic varchar(20),type varchar(10),qty integer(2),price integer(5))")
    con.commit()
    
def has(con):
    cur.execute("create table has(drug_id integer(5), phar_id integer(5),foreign key(drug_id) REFERENCES drug(drug_id))")
    con.commit()
    
def pharmacist(con):
    cur.execute("create table pharmacist(p_id integer(5),name varchar(5),phone integer(9))")
    con.commit()
    
def patient(con):
    cur.execute("create table patient(d_id integer(5) primary key,first_name varchar(20),last_name varchar(20),sex varchar(2),DOB date)")
    con.commit()

def doctor(con):
    cur.execute("create table doctor(doc_id integer(5) primary key,first_name varchar(20),last_name varchar(20),sex varchar(2),qualification varchar(20),hospital varchar(10))")
    con.commit()


def pharmacy(con):
    cur.execute("create table pharmacy(phar_id integer(5) primary key,name varchar(20),address varchar(20))")
    con.commit()
def drug(con):
    cur.execute("create table drug(drug_id integer(5) primary key,name varchar(20),generic varchar(20),type varchar(10),qty integer(2),price integer(5))")
    con.commit()
def has(con):
    cur.execute("create table has(drug_id integer(5), phar_id integer(5),foreign key(phar_id) REFERENCES drug(drug_id))")
    con.commit()
def pharmacist(con):
    cur.execute("create table pharmacist(p_id integer(5),name varchar(5),phone integer(9))")
    con.commit()
    
def patient(con):
    cur.execute("create table patient(d_id integer(5) primary key,first_name varchar(20),last_name varchar(20),sex varchar(2),DOB date)")
    con.commit()

def doctor(con):
    cur.execute("create table doctor(doc_id integer(5) primary key,first_name varchar(20),last_name varchar(20),sex varchar(2),qualification varchar(20),hospital varchar(10))")
    con.commit()

                             #insertion
def insdoc(con):
    d=int(input("Enter doctor id : "))
    f=input("Enter first name : ")
    l=input("Enter last name : ")
    s=input("Enter Sex : ")
    q=input("Enter qualification : ")
    h=input("Enter Hospital : ")
    cur.execute("insert into doctor values(?,?,?,?,?,?)",(d,f,l,s,q,h))
    con.commit()
    print("record created")
    time.sleep(2)
    cls()
    ins(con)

def insphcy(con):
    p=int(input("Enter Pharmacy ID : "))
    n=input("Enter Name : ")
    a=input("Enter Address : ")
    cur.execute("insert into pharmacy values(?,?,?)",(p,n,a))
    con.commit()
    print("record created")
    time.sleep(2)
    cls()
    ins(con)


def insphst(con):
    p=int(input("Enter pharmacist ID : "))
    n=input("Enter name : ")
    pn=int(input("Enter phone number : "))
    cur.execute("insert into pharmacist values(?,?,?)",(p,n,pn))
    con.commit()
    print("record created")
    time.sleep(2)
    cls()
    ins(con)

    
def insstck(con):
    d=int(input("Enter Drug ID : "))
    p=int(input("Enter Pharmacy ID : "))
    cur.execute("insert into has values(?,?)",(d,p))
    con.commit()
    print("record created")
    time.sleep(2)
    cls()
    ins(con)


def insdrug(con):
    d=int(input("Enter Drug ID : "))
    n=input("Enter drug name : ")
    g=input("Enter Generic : ")
    t=input("Enter Type : ")
    q=int(input("Enter Quantity"))
    p=int(input("Enter Price : "))
    cur.execute("insert into drug values(?,?,?,?,?,?)",(d,n,g,t,q,p))
    con.commit()
    print("record created")
    time.sleep(2)
    cls()
    ins(con)

    

def ins(con):
    print("Select the table to insert")
    print("1.Doctor Table")
    print("2.Pharmacy table")
    print("3.Pharmacist table")
    print("4.Drug table")
    print("5.Stock table")
    print("6.previous menu")
    n=int(input("Enter your choice"))
    if(n==1):
        cls()
        insdoc(con)
    elif(n==2):
        cls()
        insphcy(con)
    elif(n==3):
        cls()
        insphst(con)
    elif(n==4):
        cls()
        insdrug(con)
    elif(n==5):
        cls()
        insstck(con)
    elif(n==6):
        cls()
        pharm()
    else:
        print("Wrong input")
        ins(con)


                             #deletion
def deldoc(con):
    d=int(input("Enter doctor ID to delete : "))
    cur.execute("delete from doctor where doc_id=?",(d,))
    con.commit()
    print("record deleted")
    time.sleep(2)
    cls()
    delt(con)

def delphcy(con):
    p=int(input("Enter pharmacy ID to delete : "))
    cur.execute("delete from pharmacy where phar_id=?",(p,))
    con.commit()
    print("record deleted")
    time.sleep(2)
    cls()
    delt(con)

def delphst(con):
    p=int(input("Enter pharmacist ID to delete : "))
    cur.execcute("delete from pharmacist where p_id=?",(p,))
    con.commit()
    print("record deleted")
    time.sleep(2)
    cls()
    delt(con)

def deldrug(con):
    d=int(input("Enter Drug ID to delete : "))
    cur.execute("delete from drug where drug_id=?",(d,))
    con.commit()
    print("record deleted")
    time.sleep(2)
    cls()
    delt(con)

def delstck(con):
    d=int(input("Enter Drug ID to delete : "))
    cur.execute("delete from has where drug_id=?",(d,))
    con.commit()
    print("record deleted")
    time.sleep(2)
    cls()
    delt(con)
    
    
def delt(con):
    print("Select the table to delete from")
    print("1.Doctor Table")
    print("2.Pharmacy table")
    print("3.Pharmacist table")
    print("4.Drug table")
    print("5.Stock table")
    print("6.previous menu")
    n=int(input("Enter your choice"))
    if(n==1):
        cls()
        deldoc(con)
    elif(n==2):
        cls()
        delphcy(con)
    elif(n==3):
        cls()
        delphst(con)
    elif(n==4):
        cls()
        deldrug(con)
    elif(n==5):
        cls()
        delstck(con)
    elif(n==6):
        cls()
        pharm()
    else:
        print("Wrong input")
        delt(con)

                                     #updation

def upddoc(con):
    d=int(input("Enter doctor ID to update : "))
    cur.execute("delete from doctor where doc_id=?",(d,))
    f=input("Enter first name : ")
    l=input("Enter last name : ")
    s=input("Enter Sex : ")
    q=input("Enter qualification : ")
    h=input("Enter Hospital : ")
    cur.execute("insert into doctor values(?,?,?,?,?,?)",(d,f,l,s,q,h))
    con.commit()
    print("record updated")
    time.sleep(2)
    cls()
    upd(con)

def updphcy(con):
    p=int(input("Enter pharmacy ID to update : "))
    cur.execute("delete from pharmacy where phar_id=?",(p,))
    p=int(input("Enter Pharmacy ID : "))
    n=input("Enter Name : ")
    a=input("Enter Address : ")
    cur.execute("insert into pharmacy values(?,?,?)",(p,n,a))
    con.commit()
    print("record updated")
    time.sleep(2)
    cls()
    upd(con)

def updphst(con):
    p=int(input("Enter pharmacist ID to update : "))
    cur.execcute("delete from pharmacist where p_id=?",(p,))
    n=input("Enter name : ")
    pn=int(input("Enter phone number : "))
    cur.execute("insert into pharmacist values(?,?,?)",(p,n,pn))
    con.commit()
    print("record updated")
    time.sleep(2)
    cls()
    upd(con)

def upddrug(con):
    d=int(input("Enter Drug ID to update : "))
    cur.execute("delete from drug where drug_id=?",(d,))
    n=input("Enter drug name : ")
    g=input("Enter Generic : ")
    t=input("Enter Type : ")
    q=int(input("Enter Quantity"))
    p=int(input("Enter Price : "))
    cur.execute("insert into drug values(?,?,?,?,?,?)",(d,n,g,t,q,p))
    con.commit()
    print("record updated")
    time.sleep(2)
    cls()
    upd(con)

def updstck(con):
    d=int(input("Enter Drug ID to update : "))
    cur.execute("delete from has where drug_id=?",(d,))
    p=int(input("Enter Pharmacy ID : "))
    cur.execute("insert into has values(?,?)",(d,p))
    con.commit()
    print("record updated")
    time.sleep(2)
    cls()
    upd(con)
    
    
    

def upd(con):
    print("Select the table to update")
    print("1.Doctor Table")
    print("2.Pharmacy table")
    print("3.Pharmacist table")
    print("4.Drug table")
    print("5.Stock table")
    print("6.previous menu")
    n=int(input("Enter your choice"))
    if(n==1):
        cls()
        upddoc(con)
    elif(n==2):
        cls()
        updphcy(con)
    elif(n==3):
        cls()
        updphst(con)
    elif(n==4):
        cls()
        upddrug(con)
    elif(n==5):
        cls()
        updstck(con)
    elif(n==6):
        cls()
        pharm()
    else:
        print("Wrong input")
        upd(con)

        #menu for pharmacist

def pharm():
    print("Select the function")
    print("1. Insert")
    print("2. Delete")
    print("3. Update")
    print("4. Go to Mainmenu")
    n=int(input("enter your choice : "))
    if(n==1):
        cls()
        ins(con)
    elif(n==2):
        cls()
        delt(con)
    elif(n==3):
        cls()
        upd(con)
    elif(n==4):
        cls()
        mainmenu()
    else:
        print("wrong input")    

        #menu for patients

def pat(con):
    dname=input("Enter name of drug to search : ")
    cur.execute("select * from pharmacy where phar_id in (select phar_id from has where drug_id in(select drug_id from drug where name=?))",(dname,))
    records=cur.fetchall()
    print("Printing Addresses")
    time.sleep(2)
    for row in records:
        print("\n")
        print("Name : ",row[1])
        print("Address : ",row[2])
        print("\n")
    time.sleep(5)
    mainmenu()

        #main menu

def mainmenu():
    print("1.pharmacist")
    print("2.patient")
    print("3.exit")
    n=int(input("enter your choice"))
    if(n==1):
        cls()
        pharm()
    elif(n==2):
        cls()
        pat(con)
    elif(n==3):
        sys.exit()
    else:
        print("wrong input")
        mainmenu()
        
pharmacy(con)
drug(con)
has(con)
pharmacist(con)
patient(con)
doctor(con)
mainmenu()


