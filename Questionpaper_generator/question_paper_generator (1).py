from tkinter import *
from tkinter import messagebox
import random
K1=list()
K2=list()
K3=list()
K4=list()
K5=list()
K6=list()
question1=list()
root = Tk()
root.title("Question paper generator using bloom taxonomy")
root.geometry("500x700")  
def subjects():
    global subject, file_name
    subject=e.get().upper()
    file_name="C:\\Users\\Vanda\\Desktop\\subjects\\"+subject+".txt"
    print(file_name)
    try:
        with open(file_name,'r') as file:
                data = file.read().split("\n")#data contain single string seperated by \n
    except:
        messagebox.showerror("File does not exists! Please make questions list of the subject first .")
    file.close()
    for inputs in data:
        inp=inputs.split("::")
        question=inp[0]#contain question
        category=inp[1]#contain K1,K2,K3,K4,K5 OR K6
        if(category=='K1'):
                K1.append(question)#PUT IN LIST K1
        elif(category=='K2'):
                K2.append(question)#PUT IN LIST K2
        elif(category=='K3'):
                K3.append(question)#PUT IN LIST K3
        elif(category=='K4'):
                K4.append(question)#PUT IN LIST K4
        elif(category=='K5'):
                K5.append(question)#PUT IN LIST K5
        else:
                K6.append(question)#PUT IN LIST K6
    global output_text_name 
    output_text_name="C:\\Users\\Vanda\\Desktop\\subjects\\"+subject+" Question Paper.txt"
    global f 
    f = open(output_text_name,'w')
    f.close()
    f =open(output_text_name,'r+')
    myLabel2= Label(root, text="Enter the SessionYear eg:2018-2019 ")
    myLabel2.pack()
    global a
    a = Entry(root, width=50)
    a.pack()
    mybutton= Button(root, text="ok",width=25,command=session)
    mybutton.pack()

def session():
    global firstLine, sessionyear
    sessionyear = a.get().upper()
    firstLine="----------------------------------------------"+sessionyear+"----------------------------------------------\n"
    f.write(firstLine)
    myLabel3= Label(root, text="Enter the Subject Code?")
    myLabel3.pack()
    global b
    b = Entry(root, width=50)
    b.pack()
    mybutton= Button(root, text="ok",width=25,command=subject_code)
    mybutton.pack()

def subject_code():
    global secondLine,subjectcode 
    subjectcode=b.get().upper()
    secondLine="----------------------------------------"+subject+" "+subjectcode+" M.M=30------------------------------\n"
    f.write(secondLine)
    myLabel4= Label(root, text="Enter the Semester?")
    myLabel4.pack()
    global c
    c = Entry(root, width=50)
    c.pack()
    mybutton= Button(root, text="ok",width=25,command=semester)
    mybutton.pack()

def semester():
    global thirdLine,sem
    sem=c.get().upper()
    thirdLine="----------------------------------------------Semester-"+sem+"---------------------------------------------\n"
    f.write(thirdLine)
    f.write("PART A\n")#part a
    print("working")
    global cnt
    cnt=1
    count=cnt 
    myLabel5= Label(root, text="Enter the level for the ("+(str)(count)+") question")
    myLabel5.pack()
    global g
    g = Entry(root, width=50)
    g.pack()
    mybutton = Button(root, text="ok",width=25,command=lambda: gets(1))
    mybutton.pack()
    cnt=2
    count=cnt 
    myLabel6= Label(root, text="Enter the level for the ("+(str)(count)+") question")
    myLabel6.pack()
    h = Entry(root, width=50)
    h.pack()
    mybutton = Button(root, text="ok",width=25,command=lambda: gets(2))
    mybutton.pack()
    cnt=3
    count=cnt 
    myLabel7= Label(root, text="Enter the level for the ("+(str)(count)+") question")
    myLabel7.pack()
    i = Entry(root, width=50)
    i.pack()
    mybutton = Button(root, text="ok",width=25,command=lambda: gets(3))
    mybutton.pack()
    cnt=4
    count=cnt 
    myLabel8= Label(root, text="Enter the level for the ("+(str)(count)+") question")
    myLabel8.pack()
    j = Entry(root, width=50)
    j.pack()
    mybutton = Button(root, text="ok",width=25,command=lambda: gets(4))
    mybutton.pack()
    cnt=5
    count=cnt 
    myLabel9= Label(root, text="Enter the level for the ("+(str)(count)+") question")
    myLabel9.pack()
    k = Entry(root, width=50)
    k.pack()
    mybutton = Button(root, text="ok",width=25,command=lambda: gets(5))
    mybutton.pack()
    cnt=6
    count=cnt 
    myLabel10= Label(root, text="Enter the level for the ("+(str)(count)+") question")
    myLabel10.pack()
    l = Entry(root, width=50)
    l.pack()
    mybutton = Button(root, text="ok",width=25,command=lambda: gets(6))
    mybutton.pack()
    f.write("PART B\n")
    cnt=7
    count=cnt 
    myLabel11= Label(root, text="Enter the level for the ("+(str)(count)+") question")
    myLabel11.pack()
    m = Entry(root, width=50)
    m.pack()
    mybutton = Button(root, text="ok",width=25,command=lambda: getss(7))
    mybutton.pack()
    cnt=8
    count=cnt 
    myLabel10= Label(root, text="Enter the level for the ("+(str)(count)+") question")
    myLabel10.pack()
    n = Entry(root, width=50)
    n.pack()
    mybutton = Button(root, text="ok",width=25,command=lambda: getss(8))
    mybutton.pack()
    mybutton = Button(root, text="exit",width=25,command=root.quit)
    mybutton.pack()
    
def getss(num):
    global level
    level=g.get().upper()
    choices(num)
    print("hdjesbdkbskjdb")
    return
def choices(num):
    i=num
    while True:
        if level=="K1":
            ques=random.choice(K1)
            if ques in question1:
                continue
            else:
                question1.append(ques)
                temp_str=(str)(i)+")"+ques+"    [10M]\n"
                f.write(temp_str)
                i=i+1
                break
        elif level=="K2":
            ques=random.choice(K2)
            if ques in question1:
                continue
            else:
                question1.append(ques)
                temp_str=(str)(i)+")"+ques+"    [10M]\n"
                f.write(temp_str)
                i=i+1
                break
        elif level=="K3":
            ques=random.choice(K3)
            if ques in question1:
                continue
            else:
                question1.append(ques)
                temp_str=(str)(i)+")"+ques+"    [10M]\n"
                f.write(temp_str)
                i=i+1
                break
        elif level=="K4":
            ques=random.choice(K4)
            if ques in question1:
                continue
            else:
                question1.append(ques)
                temp_str=(str)(i)+")"+ques+"    [10M]\n"
                f.write(temp_str)
                i=i+1
                break
        elif level=="K5":
            ques=random.choice(K5)
            if ques in question1:
                continue
            else:
                question1.append(ques)
                temp_str=(str)(i)+")"+ques+"    [10M]\n"
                f.write(temp_str)
                i=i+1
                break
        elif level=="K6":
            ques=random.choice(K6)
            if ques in question1:
                continue
            else:
                question1.append(ques)
                temp_str=(str)(i)+")"+ques+"    [10M]\n"
                f.write(temp_str)
                i=i+1
                break
        else:
            print("Enter only from K1-K6!!")
            break
    return

def choice(num):
    count=num
    while True:
        if level=="K1":
                ques=random.choice(K1)
                if ques in question1:
                    continue
                else:
                    question1.append(ques)
                    temp_str=(str)(count)+")"+ques+"    [10M]\n"
                    print("fdsfdsfsfsefesfse")
                    f.write(temp_str)
                    if (count % 2) == 0:
                        count=count+1
                        f.write("\n")
                        break
                    else:
                        OR="OR\n"
                        f.write(OR)
                        count=count+1
                        break
        elif level=="K2":
                ques=random.choice(K2)
                if ques in question1:
                    continue
                else:
                    question1.append(ques)   
                    temp_str=(str)(count)+")"+ques+"    [10M]\n"
                    f.write(temp_str)
                    if (count % 2) == 0:
                        count=count+1
                        f.write("\n")
                        break
                    else:
                        OR="OR\n"
                        f.write(OR)
                        count=count+1
                        break
        elif level=="K3":
                ques=random.choice(K3)
                if ques in question1:
                    continue
                else:
                    question1.append(ques)
                    temp_str=(str)(count)+")"+ques+"    [10M]\n"
                    f.write(temp_str)
                    if (count % 2) == 0:
                        count=count+1
                        f.write("\n")
                        break
                    else:
                        OR="OR\n"
                        f.write(OR)
                        count=count+1
                        break
        elif level=="K4":
                ques=random.choice(K4)
                if ques in question1:
                    continue
                else:
                    question1.append(ques)
                    temp_str=(str)(count)+")"+ques+"    [10M]\n"
                    f.write(temp_str)
                    if (count % 2) == 0:
                        count=count+1
                        f.write("\n")
                        break
                    else:
                        OR="OR\n"
                        f.write(OR)
                        count=count+1
                        break
        elif level=="K5":
                ques=random.choice(K5)
                if ques in question1:
                    continue
                else:
                    question1.append(ques)
                    temp_str=(str)(count)+")"+ques+"    [10M]\n"
                    f.write(temp_str)
                    if (count % 2) == 0:
                        count=count+1
                        f.write("\n")
                        break
                    else:
                        OR="OR\n"
                        f.write(OR)
                        count=count+1
                        break
        elif level=="K6":
                ques=random.choice(K6)
                if ques in question1:
                        continue
                else:
                    question1.append(ques)
                    temp_str=(str)(count)+")"+ques+"    [10M]\n"
                    f.write(temp_str)
                    if (count % 2) == 0:
                        count=count+1
                        f.write("\n")
                        break
                    else:
                        OR="OR\n"
                        f.write(OR)
                        count=count+1
                        break
        else:
                messagebox.showerror("File does not exists! Please make questions list of the subject first .")
                break
    return
        
def gets(num):
    global level
    level=g.get().upper()
    choice(num)
    print("hdjesbdkbskjdb")
    return
    
myLabel1 = Label(root, text="Enter the Subject Name for which you want to generate question paper?")
myLabel1.pack()
e = Entry(root, width=50)
e.pack()
mybutton= Button(root, text="ok",width=25,command=subjects)
mybutton.pack()
root.mainloop()
f.close()
