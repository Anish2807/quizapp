from mail2 import *
import pymysql

print("--------------Welcome to the flight booking reservation system----------------------")

mydb=pymysql.connect(host="localhost",user="root",password="",port=3306,database="flight_booking")
mycur=mydb.cursor()
def callAdmin():
    while True:
        print("1.add flight sechedule: ")
        print("2.view passenger: ")
        print("3.view avilable seat: ")
        print("4.Logout: ")
        ch= int(input("Enter Choice Num: "))
        if ch==1:
        
            name=input("Enter flight Name: ")
            opoint=input("Enter Origin Point: ")
            otime=input("Enter departure time: ")
            dpoint=input("Enter destination point: ")
            dtime=input("Enter destination time: ")
            droppoint=input("Enter drop point Point: ")
            droptime=input("Enter drop time: ")
            fcost=input("Enter cost:")
            dcost=input("Enter drop cost:")
            seat=10
            mycur.execute("insert into fligtlist(fname,seat,opoint,despoint,dropoint,d_time,a_time,dr_time,dropcost, cost) values('{}',{},'{}','{}', '{}', '{}','{}','{}', '{}', '{}')".format(name,seat,opoint,dpoint,droppoint,dtime,otime,droptime,dcost,fcost))
            mydb.commit()
            print("Flight Added!")


        elif ch==2:
            mycur.execute("select * from booking")
            data=mycur.fetchall()
            for i in data:
                print(i)

            
        elif ch==3:
            l=[]
            date = input("Enter date(dd/mm/yyy): ")
            fno=int(input("Enter flight no: "))
            mycur.execute("select * from booking")
            data=mycur.fetchall()
            

            for i in data:
                if i[6]==date and i[9]==fno:
                    print("booked seat no: ",i[7])
                    
                    
                else:
                    print("total no of seat avilable is 10")
        elif ch==4:
            break
    
def callUser():
    while True:
        print("1.view flight sechedule: ")
        print("2.view avilable seat: ")
        print("3.book ticket: ")
        print("4.cancle ticket: ")
        print("5.send your ticket on your mail: ")
        print("6. logout ")
        ch=int(input("Enter your choice: "))
        if ch==1:
            mycur.execute("select * from fligtlist")
            data=mycur.fetchall()

            for i in data:

                print("==Name==Seat==From==To==Drop==Des_Time==Origin_Time==Drop_Time==Drop_Cost==Full_Cost==")

                print(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],)

        elif ch==2:
            l=[]
            date = input("Enter date(dd/mm/yyy): ")
            fno=int(input("Enter flight no: "))
            mycur.execute("select * from booking")
            data=mycur.fetchall()
            

            for i in data:
                if i[6]==date and i[9]==fno:
                    print("booked seat no: ",i[7])
                    
                    
                else:
                    print("total no of seat avilable is 10")
        elif ch==3:
            un=input("Enter Username: ")
            pwd=input("Enter Password: ")
            mycur.execute("select * from admin where username='{}' and password='{}'".format(un,pwd))
            data=mycur.fetchone()
            if data[4]=="passenger":
                print("welcome user",data[2])

            mycur.execute("select * from fligtlist")
            data1=mycur.fetchall()

            for i in data1:

                print("fid==Name==Seat==From==To==Drop==Des_Time==Origin_Time==Drop_Time==Drop_Cost==Full_Cost==")

                print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],)
            fid=int(input("Enter flight ID: "))
            un=input("Enter Name: ")
            age=int(input("Enter Age: "))
            mob=input("Enter Mobile Number: ")
            ori=input("Enter Origin Place: ")
            sno=int(input("Enter seat no(1-10): "))
            des=input("Enter Destination Place: ")
            date=input("Enter date of journey(dd/mm/yyyy): ")
            cost=input("Enter Amount: ")
                

            mycur.execute("insert into booking(uname,age,mob,origin,destination,doj,sno,cost,flightID)values('{}',{},'{}','{}','{}','{}',{},'{}',{})".format(un,age,mob,ori,des,date,sno,cost,fid))
            mydb.commit()
            print("tikat book ho gya:")
            
            
        elif ch==4:
            un=input("Enter your name:")
            fno=input("Enter flight no: ")
            mycur.execute("delete from booking where uname='{}'".format(un))
            mydb.commit()
            print("cancle tikat: ")
            
        elif ch==5:
            
            un=input("Enter your name: ")
            mycur.execute("select * from booking where uname='{}'".format(un))
            data=mycur.fetchone()
            
            message =str(data)

            s.sendmail("anish4726@gmail.com","anishlnct12@gmail.com",message)

            s.quit()

            
        elif ch==6:
            break


while True:
    
    print("press 1 for create userId/pass login:")
    print("press 2 for admin/passenger login: ")
    print("press 3 for exit : ")
    print("*********************************")
    ch=int(input("Enter The Choice: "))
    if ch==2:
        un=input("Enter Username: ")
        pwd=input("Enter Password: ")
        mycur.execute("select * from admin where username='{}' and password='{}'".format(un,pwd))
        data=mycur.fetchone()
        if data:
            print("welcome",data[2])
            print("==================")
        if data[4]=="admin":
            callAdmin()
        elif data[4]=="passenger":
            callUser()
        else:
            print("Invalid data")

    elif ch==1:
        un=input("User Name: ")
        name=input("Enter Pansseger Name: ")
        pd=input("Enter Password: ")
        usertype='passenger'
        mycur.execute("insert into admin(username,name, password,usertype) values('{}','{}','{}','{}')".format(un,name,pd,usertype))
        mydb.commit()
        print("==================")
        
        
        print("Added sucessful")
    elif ch==3:
        print("Thanku to visit: ")
        break
