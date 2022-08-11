from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter import ttk



# Add your own database name and password here to reflect in the code
mypass = ""
mydatabase="DiaManagement1"

# Enter Table Names here
userTable = "User1" #User1 Table
root = Tk()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
   database="DiaManagement1"
 
)
def setStyle(root):
    style = ttk.Style(root)
    style.configure('.',font=('Baskerville', 20,))

cur = mydb.cursor()

root.title("Diabetic management system")
root.minsize(width=400,height=400)
root.geometry("1000x1000")
root['bg']='pink'
id =0
count = 0
MenuCount = 0
def CheckDiabetes():
    root.destroy()
    import Predict

def Menu():

    global headingFrame1,headingFrame2,headingLabel,labelFrame,backBtn,SubmitBtn,MenuCount
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    SubmitBtn.destroy()
    labelFrame.destroy()
    MenuCount += 1

    labelFrame = Frame(root,bg='pink')
    labelFrame.place(relx=0.01,rely=0.05,relwidth=0.80,relheight=0.9)

    headingFrame1 = Frame(labelFrame,bg="#333945",bd=5)
    headingFrame1.place(relx=0.37,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    headingLabel = Label(headingFrame2, text="MENU", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
    btn1 = Button(labelFrame,text="Check Diabetes ",bg='light green', fg='black',command = CheckDiabetes)
    btn1.place(relx=0.4,rely=0.3, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(labelFrame,text="Plan Meals",bg='light green', fg='black', command =foodPlanSubWindow )
    btn2.place(relx=0.4,rely=0.4, relwidth=0.45,relheight=0.1)
    
    backBtn = Button(labelFrame,text="Logout",bg='#455A64', fg='white', command=HomePage)
    backBtn.place(relx=0.5,rely=0.58, relwidth=0.18,relheight=0.08)
    
def foodPlanAddWindow():
    fp2_sub_window = Toplevel()
    fp2_sub_window.title('FOOD PLAN')
    fp2_sub_window.geometry("630x420+450+250")

    setStyle(fp2_sub_window)
    global login
    topFrame = Frame(fp2_sub_window)
    topFrame.grid(row=4,column=0)
    bottomFrame = Frame(fp2_sub_window)
    bottomFrame.grid(row=18,column=0)

    Carb_label = ttk.Label(topFrame, text = "Carbohydrates : ", font=('Baskerville',20))
    Carb_label.grid(row=1,column=0,sticky='NSWE')
    Carb_entry = ttk.Entry(topFrame, font=('Baskerville',20))
    Carb_entry.grid(row=1,column=1,sticky='NSWE')
    Pro_label = ttk.Label(topFrame, text = "Proteins: ", font=('Baskerville',20))
    Pro_label.grid(row=3,column=0,sticky='NSWE')
    Pro_entry = ttk.Entry(topFrame, font=('Baskerville',20))
    Pro_entry.grid(row=3,column=1,sticky='NSWE')
    Fat_label = ttk.Label(topFrame, text = "Fats: ", font=('Baskerville',20))
    Fat_label.grid(row=5,column=0,sticky='NSWE')
    Fat_entry = ttk.Entry(topFrame, font=('Baskerville',20))
    Fat_entry.grid(row=5,column=1,sticky='NSWE')
    
    
    def fp2_submit():
        Carb=float(Carb_entry.get())
        Pro=float(Pro_entry.get())
        Fat=float(Fat_entry.get())
        Nutr=Carb+Pro+Fat
        meal_entry = "INSERT INTO Meal1 VALUES(%s,curdate(),curtime(),%s,%s,%s,%s)"
        val = (login[0], Carb,Pro,Fat,Nutr)
        try:
            cur.execute(meal_entry, val)
            mydb.commit()
            messagebox.showinfo("You have successfully registered. Now you can login using same details.")
            
        except:
           messagebox.showinfo("Error inserting","Cannot add data to Database")

    back = ttk.Button(bottomFrame, text="BACK",command=lambda:fp2_sub_window.destroy())
    back.grid(row=4,column=1,sticky='NSEW',ipady=10, ipadx=20)
    submit = ttk.Button(bottomFrame, text="SUBMIT",command=fp2_submit)
    submit.grid(row=4,column=2,sticky='NSEW',ipady=10, ipadx=20)

def foodPlanSubWindow():
    fp_sub_window = Toplevel()
    fp_sub_window.title('FOOD PLAN')
    fp_sub_window.geometry("630x420+450+250")
    global login
    setStyle(fp_sub_window)

    topFrame = Frame(fp_sub_window)
    topFrame.grid(row=9,column=0)
    bottomFrame = Frame(fp_sub_window)
    bottomFrame.grid(row=18,column=0)

    display = Listbox(topFrame, font=('Baskerville',20))
    display.pack(fill=BOTH, expand=YES, side=LEFT)
    scroll = Scrollbar(topFrame)
    scroll.pack(side=RIGHT, fill=Y, expand=NO)
    scroll.configure(command=display.yview)
    display.configure(yscrollcommand=scroll.set)

    get_fp_rows = "SELECT * FROM Meal1 where userid=%s"
    cur.execute(get_fp_rows,login)
    for item in cur:
        display.insert(END, item[0],item[1],item[2],item[6],' ')

    fp_add = ttk.Button(bottomFrame, text = "ADD", command=foodPlanAddWindow)
    fp_add.grid(row=0,column=0,sticky='NSEW',ipady=10, ipadx=50)
    back = ttk.Button(bottomFrame, text="BACK",command=lambda:fp_sub_window.destroy())
    back.grid(row=0,column=1,sticky='NSEW',ipady=10, ipadx=20)

def gettingDetails():
    
    Name = en1.get()
    password = en2.get()
    sql = "INSERT INTO user1 (username,userpass) VALUES (%s, %s)"
    val = (Name, password)
     
    try:
        cur.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("You have successfully registered. Now you can login using same details.")
        HomePage()
    except:
        messagebox.showinfo("Error inserting","Cannot add data to Database")
        
    print(Name)
    print(password)
    en1.delete(0, END)
    en2.delete(0, END)


def Register():
    
    global labelFrame,SubmitBtn
    
    global count
    count += 1

    if(count>=2):
        labelFrame.destroy()
    
    global en1,en2
    
    labelFrame = Frame(root,bg='#044F67')
    labelFrame.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.80)
    
    #User Name
    lb1 = Label(labelFrame,text="Full Name : ", bg='#044F67', fg='white')
    lb1.place(relx=0.05,rely=0.2)
    
    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    
    # User Password
    lb3 = Label(labelFrame,text="Password : ", bg='#044F67', fg='white')
    lb3.place(relx=0.05,rely=0.35)
    
    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.35, relwidth=0.62)
    
    
    #Submit Button
    SubmitBtn = Button(labelFrame,text="SUBMIT",bg='#264348', fg='white',command=gettingDetails)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

def gettingLoginDetails():
    global login
    login = (int(en1.get()),)
    name = (en2.get(),)
    password = (en3.get(),) 

    try:
            cur.execute("select userid from user1 where userpass = %s",password)
            myresult1 = cur.fetchall()
            for i in myresult1:
                getLoginID = i[0]
            cur.execute("select username from user1 where userpass =%s",password)
            myresult2 = cur.fetchall()
            for i in myresult2:
                getName = i[0]

            if(getLoginID == login[0] and getName == name[0]):
                Menu()
                messagebox.showinfo("SUCCESS","You have successfully logged in")
            else:
                messagebox.showerror("Failure","Can't log in, check your credentials")
    except:
            messagebox.showinfo("FAILED","Please check your credentials")
        
    print(login)
    print(name)
    print(password)
    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)

def Login():
    global labelFrame,SubmitBtn,en1,en2,en3
    
    global count
    count += 1

    if(count>=2):
        labelFrame.destroy()
    
    labelFrame = Frame(root,bg='#044F67')
    labelFrame.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.80)
    
    #User Name
    lb1 = Label(labelFrame,text="USer ID : ", bg='#044F67', fg='white')
    lb1.place(relx=0.05,rely=0.2)
    
    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    
    # User Password
    lb2 = Label(labelFrame,text="User Name : ", bg='#044F67', fg='white')
    lb2.place(relx=0.05,rely=0.35)
    
    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.35, relwidth=0.62)

    lb3 = Label(labelFrame,text="Password : ", bg='#044F67', fg='white')
    lb3.place(relx=0.05,rely=0.5)
    
    en3 = Entry(labelFrame)
    en3.place(relx=0.3,rely=0.5, relwidth=0.62)
    #Submit Button
    SubmitBtn = Button(labelFrame,text="SUBMIT",bg='green', fg='black',command=gettingLoginDetails)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    

def HomePage():
    
    global headingFrame1,headingFrame2,headingLabel,btn1,backBtn,btn2,labelFrame,count
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    btn2.destroy()

    if(count>=1):
        labelFrame.destroy()
    
    if(MenuCount>=1):
        btn1.destroy()
        backBtn.destroy()

    headingFrame1 = Frame(root,bg="pink",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
    
    headingLabel = Label(headingFrame2, text="Hello, user", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
    btn1 = Button(root,text="Register",bg='black', fg='white',command=Register)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.2,relheight=0.1)
    
    btn2 = Button(root,text="Login",bg='black', fg='white', command=Login)
    btn2.place(relx=0.53,rely=0.3, relwidth=0.2,relheight=0.1)
    
    btn3 = Button(root,text="Quit",bg='#455A64', fg='white', command=root.quit)
    btn3.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

n=0.3

headingFrame1 = Frame(root,bg="black",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingFrame2 = Frame(headingFrame1,bg="light blue")
headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

headingLabel = Label(headingFrame2, text="Welcome to Diabetic Managemnt System", fg='black')
headingLabel.place(relx=0.25,rely=0.1, relwidth=0.5, relheight=0.5)


btn2 = Button(root,text="Get Started!!",bg='blue', fg='black', command = HomePage)
btn2.place(relx=0.40,rely=0.4, relwidth=0.2,relheight=0.1) 

btn3 = Button(root,text="Quit",bg='red', fg='black', command=root.quit)
btn3.place(relx=0.40,rely=0.6, relwidth=0.2,relheight=0.1)

root.mainloop()