''' CODSOFT Internship - PYTHON PROGRAMMING 
    TASK 1 - TO-DO LIST
    DONE BY MONEESH S
'''

import tkinter #for creating layout

from tkinter import*
#here we can able to set the frame title,dimensions,pixels,fixing the frame and its background
root =Tk()
root.title("TO-DO-LIST by Moneesh S")
root.geometry("700x670+400+200")
root.resizable(False,False)
root.configure(bg="#ffc0cb")

duty_list=[]

#function for add the input characters given by the user [CREATE]
def addDuty():
    task=duty_in.get()
    duty_in.delete(0, END)

    if task:
        with open("tasklist.txt","a") as dutyfile:
            dutyfile.write(f"\n{task}")
        duty_list.append(task)
        listbox.insert(END,task)

#function for delete the task which will remove by the user [DELETE OR UPDATE]
def deleteDuty():
    global duty_list
    task=str(listbox.get(ANCHOR))
    if task in duty_list:
        duty_list.remove(task)
        with open ("tasklist.txt","w") as dutyfile:
            for task in duty_list:
                dutyfile.write(task+"\n")
        
        listbox.delete(ANCHOR)

#function to maintain the tasks until the user gives their input           
def openDutyFile():
        try:
            global duty_list
            with open ("tasklist.txt","r") as dutyfile:
                tasks= dutyfile.readlines()

            for task in tasks:
                if task != '\n':
                    duty_list.append(task)
                    listbox.insert(END,task)

        except:
            file=open("tasklist.txt","w")
            file.close()

#creating application icon
app_icon = PhotoImage(file="Image/task.png")
root.iconphoto(False,app_icon)

#creating the title name,font,size,background,position
topic=Label(root,text="TODO-LIST",font="Bazooka 40 ",fg="black",bg="#ffc0cb")
topic.place(x=190,y=30)

#for receiving the user input
frame=Frame(root,width=680,height=50,bg="white")
frame.place(x=10,y=140)

#create font and its size, boldness, position
duty=StringVar()
duty_in=Entry(frame,width=18,font="arial 20",bd=0)
duty_in.place(x=10,y=7)

#creating add button to add the input in list which was given by the user
button=Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#005D83",fg="#ffffff",bd=0,command=addDuty)
button.place(x=573,y=0)

#create the bigbox for add,delete,update the user input
frame1=Frame(root,bd=0,width=300,height=40,bg="#005D83")#box width,height,background
frame1.pack(pady=(260,0))

#Creating the cursor type , box height, width
listbox= Listbox(frame1,font=('Bazooka',12),width=69,height=16,bg="#005D83",fg="white",cursor="hand2",selectbackground="#5a96ff")
listbox.pack(side=LEFT , fill=BOTH,  padx=3)
#creating scrollbar
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT , fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

#for showing the added task when opening the application
openDutyFile()

#delete
Trash_icon=PhotoImage(file="Image/delete.png")
Button(root,image=Trash_icon,bd=0,command=deleteDuty,bg="#ffc0cb",fg="#6883BC").pack(side=BOTTOM,pady=12)

#for the excution of program in loop condition
root.mainloop()