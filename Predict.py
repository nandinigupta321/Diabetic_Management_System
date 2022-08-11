import tkinter as tk
import pandas as pd
from tkinter import ttk
import joblib
win = tk.Tk() #create instance of tkinter frame

win.title('Diabetes Predictions')
win.geometry("1000x1000")
win['bg']='light blue'
Preg=ttk.Label(win,text="Preg")
Preg.grid(row=0,column=0,sticky=tk.W, padx=10,
               pady=10,
               ipadx=10,
               ipady=10)
Preg_var=tk.StringVar()
Preg_entrybox=ttk.Entry(win,width=30,textvariable=Preg_var)
Preg_entrybox.grid(row=0,column=1, padx=10,
               pady=10,
               ipadx=10,
               ipady=10)
#Column 2
Plas=ttk.Label(win,text="Plas")
Plas.grid(row=1,column=0,sticky=tk.W, padx=10,
               pady=10,
               ipadx=10,
               ipady=10)
Plas_var=tk.StringVar()
Plas_entrybox=ttk.Entry(win,width=30,textvariable=Plas_var)
Plas_entrybox.grid(row=1,column=1, padx=10,
               pady=10,
               ipadx=10,
               ipady=10)
#Column 3
Pres=ttk.Label(win,text="Pres")
Pres.grid(row=2,column=0,sticky=tk.W, padx=10,
               pady=10,
               ipadx=10,
               ipady=10)
Pres_var=tk.StringVar()
Pres_entrybox=ttk.Entry(win,width=30,textvariable=Pres_var)
Pres_entrybox.grid(row=2,column=1, padx=10,
               pady=10,
               ipadx=10,
               ipady=10)
#Column 4
skin=ttk.Label(win,text="skin")
skin.grid(row=3,column=0,sticky=tk.W, padx=10,
               pady=10,
               ipadx=10,
               ipady=10)
skin_var=tk.StringVar()
skin_entrybox=ttk.Entry(win,width=30,textvariable=skin_var)
skin_entrybox.grid(row=3,column=1, padx=10,
               pady=10,
               ipadx=10,
               ipady=10)
#Column 5
test=ttk.Label(win,text="test")
test.grid(row=4,column=0,sticky=tk.W, padx=10,
               pady=10,
               ipadx=10,
               ipady=10)
test_var=tk.StringVar()
test_entrybox=ttk.Entry(win,width=30,textvariable=test_var)
test_entrybox.grid(row=4,column=1, padx=10,
               pady=10,
               ipadx=10,
               ipady=10)
#Column 6
mass=ttk.Label(win,text="mass")
mass.grid(row=5,column=0,sticky=tk.W, padx=10,
               pady=10,
               ipadx=10,
               ipady=10)
mass_var=tk.StringVar()
mass_entrybox=ttk.Entry(win,width=30,textvariable=mass_var)
mass_entrybox.grid(row=5,column=1, padx=10,
               pady=10,
               ipadx=10,
               ipady=10)
#Column 7
pedi=ttk.Label(win,text="pedi")
pedi.grid(row=6,column=0,sticky=tk.W, padx=10,
               pady=10,
               ipadx=10,
               ipady=10)
pedi_var=tk.StringVar()
pedi_entrybox=ttk.Entry(win,width=30,textvariable=pedi_var)
pedi_entrybox.grid(row=6,column=1, padx=10,
               pady=10,
               ipadx=10,
               ipady=10)
#Column 8
age=ttk.Label(win,text="age")
age.grid(row=7,column=0,sticky=tk.W, padx=10,
               pady=10,
               ipadx=10,
               ipady=10)
age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=30,textvariable=age_var)
age_entrybox.grid(row=7,column=1, padx=10,
               pady=10,
               ipadx=10,
               ipady=10)


def Output():
    DF = pd.DataFrame()
    global DB
    DF = pd.DataFrame(columns=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'])
    PREG=Preg_var.get()
    DF.loc[0,'Pregnancies']=PREG
    PLAS=Plas_var.get()
    DF.loc[0,'Glucose']=PLAS
    PRES=Pres_var.get()
    DF.loc[0,'BloodPressure']=PRES
    SKIN=skin_var.get()
    DF.loc[0,'SkinThickness']=SKIN
    TEST=test_var.get()
    DF.loc[0,'Insulin']=TEST
    MASS=mass_var.get()
    DF.loc[0,'BMI']=MASS
    PEDI=pedi_var.get()
    DF.loc[0,'DiabetesPedigreeFunction']=PEDI
    AGE=age_var.get()
    DF.loc[0,'Age']=AGE
    print(DF.shape)
    DB=DF
    DB["Pregnancies"] = pd.to_numeric(DB["Pregnancies"])
    DB["Glucose"] = pd.to_numeric(DB["Glucose"])
    DB["BloodPressure"] = pd.to_numeric(DB["BloodPressure"])
    DB["SkinThickness"] = pd.to_numeric(DB["SkinThickness"])
    DB["Insulin"] = pd.to_numeric(DB["Insulin"])
    DB["BMI"] = pd.to_numeric(DB["BMI"])
    DB["DiabetesPedigreeFunction"] = pd.to_numeric(DB["DiabetesPedigreeFunction"])
    DB["Age"] = pd.to_numeric(DB["Age"])
    loaded_model = joblib.load('finalized_model.pkl')
    result = loaded_model.predict(DB)
    Predict_entrybox=ttk.Entry(win,width=20)
    Predict_entrybox.grid(row=20,column=1, padx=10,
               pady=10,
               ipadx=10,
               ipady=10)
    if loaded_model.predict(DB)==1:
            result='Diabetic'
    elif loaded_model.predict(DB)==0:
            result='Non-Diabetic'
    Predict_entrybox.insert(1,str(result))
    
Predict_button=ttk.Button(win,width=20,text="Predict",command=Output)

Predict_button.grid(row=20,column=0, padx=10,
               pady=10,
               ipadx=10,
               ipady=10)
back = ttk.Button(win, text="BACK",command=lambda:win.destroy())
back.grid(row=22,column=1,sticky='NSEW',ipady=10, ipadx=20)               
    
win.mainloop()

