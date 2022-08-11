import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="DiaManagement1" #first time comment krna 
 
)

cur = mydb.cursor()
#cur.execute("CREATE DATABASE DiaManagement")

#cur.execute("SHOW DATABASES")

#for x in cur:
 #   print(x)

#cur.execute("CREATE TABLE User (userid INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), userpass VARCHAR(255))")
#sql = "INSERT INTO user1 (username,userpass) VALUES (%s, %s)"
#val = ("Nandini","1234")
#cur.execute("CREATE TABLE Meal1 (userid int ,DateTaken date, TimeTaken time, Carbs float, protein float, fat float, nutr float, Primary Key(DateTaken, TimeTaken),FOREIGN KEY(userid) REFERENCES user1(userid))")
sql = "INSERT INTO Meal1 VALUES (%s,curdate(),curtime() ,%s,%s,%s,%s)"
val = ("2",40,50,120,54)
cur.execute(sql, val)
mydb.commit()
print(cur.rowcount, "record inserted.")
     
#cur.execute(sql, val)
#mydb.commit()
#print(cur.rowcount, "record inserted.")

#p = ("1234",)
#cur.execute("select userid from user where userpass = %s",p)
#myresult1 = cur.fetchall()
           
#for i in myresult1:
 #   getLoginID = i[0]
#cur.execute("select username from user where userpass = '1234'")
#myresult2 = cur.fetchall()
#for i in myresult2:
 # getName = i[0]
            
#print(getLoginID)
#print(getName)
#if(getLoginID == 1 and getName == "JohnWoe"):
  #  print("SUCCESS","You have successfully logged in")



        