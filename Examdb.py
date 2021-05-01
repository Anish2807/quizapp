#from mail2 import *
import pymysql
import datetime
myDB = pymysql.connect(host="localhost",user="root",passwd="",port=3306,database="5_30quizdb")
myCursor=myDB.cursor()

def getTechId():
   myCursor.execute("select * from technology")
   techs=myCursor.fetchall()
   for i in techs:
      print(i[0],i[1])
   tid=int(input("select Technology: "))
   return tid
def callAdmin():
   # print("Tu hai Admin!")
   while True:
       print("1. Add Student")
       print("2. Add Technology")
       print("3. Add Question")
       print("4. Add Results")
       print("5. Logout")
       ch = int(input("Enter your choice: "))
       if ch==1:
          try:
         
             unname=input("Enter your user name: ")
             pwd=input("Enter Password: ")
             name=input("Enter your name: ")
             role="Student"


             myCursor.execute("insert into user_profile(username,password,name,role) values ('{}','{}','{}','{}')".format(unname,pwd,name,role))
             myDB.commit()
             print("Added Student!")
          except:
             print("Student Allready Exit: ")
           
       elif ch==2:
          try:
              tn=input("Enter Technology: ")
              myCursor.execute("insert into technology(tname) values ('{}')".format(tn))
              myDB.commit()
              print("Technology Added! ")
          except:
             print("Technology Already Exit!")
       elif ch==3:
          tid= getTechId()
          q=input("Enter Question: ")
          a=input("Enter Option A: ")
          b=input("Enter Option B: ")
          c=input("Enter Option C: ")
          d=input("Enter Option D: ")
          correct=input("Enter correct Option (A/B/C/D): ")
          myCursor.execute("insert into questions(question,opta,optb,optc,optd,correct,tech_id) values('{}','{}','{}','{}','{}','{}',{})".format(q,a,b,c,d,correct,tid))
          myDB.commit()
          print("Question Added! ")
       elif ch ==4:
          print("press 1 for result by user id: ")
          print("press 2 for all result: ")
          c=int(input("enter your choice: "))
          if c==1:
             print("****************")
             id=int(input("Enter your ID: "))
             
             myCursor.execute("select * from results where user_id={}".format(id))
             data1=myCursor.fetchall()
             print("---name----marks---date---",data1)
             """
             for i in data1:
                myCursor.execute("select * name from user_profile where uid={}".format(i[1]))
                dataa = myCursor.fetchone()
                print(i[1],dataa[0],i[3],i[4])
                """
          elif c==2:
             myCursor.execute("select * from results")
             data4=myCursor.fetchall()
             print("---")
             print(data4)
                
       elif ch==5:
           break
       
def callStudent(userid):
    while True:
       print("1. Start Quiz")
       print("2. Result ")
       print("3. Logout ")

       ch=int(input("Enter Your choice: "))
       if ch==1:
          tid=getTechId()
          
          myCursor.execute("select * from questions where tech_id='{}'".format(tid))
          all_ques=myCursor.fetchall()
          j=1
          count=0
          for i in all_ques:
             print("Question",j,i[1])
             print("A",i[2])
             print("B",i[3])
             print("C",i[4])
             print("D",i[5])

             ans=input("Enter Ans: ")
             if ans == i[6]:
                count +=1
             j += 1
          print("Result: ",count,"/",len(all_ques))
          marks = (count/len(all_ques))*100
          d=datetime.date.today()
          myCursor.execute("insert into results (user_id,tech_id,marks,resdate) values ({},{},{},'{}')".format(data[0],tid,marks,d))
          myDB.commit()
          print("----------------")
          print("Your result is: ",marks)
         
       elif ch ==2:
          myCursor.execute("select * from results where user_id={}".format(data[0]))
          data3=myCursor.fetchall()
          print("****************")
          for i in data3:
             print("marks",i[3],"date",i[4])
             print("***************")
          if marks>=40.00:
             print("Congratulation! You are Pass ")
       elif ch ==3:
          break
uname = input("Enter UserName: ")
pwd = input("Enter password: ")

myCursor.execute("select * from user_profile where username='{}' and password='{}'".format(uname,pwd))
data=myCursor.fetchone()
if data:
   print("Welcome",data[3])
   if data[4] == "admin":
      
      callAdmin()
   elif data[4] == "Student":
      callStudent(data[0])

else:
   print("invalid userid")





   
