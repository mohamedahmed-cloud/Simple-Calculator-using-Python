import tkinter,os
import tkinter.messagebox
window=tkinter.Tk()


# Setting for all
window.title("Calculator 😊")
window.minsize(500,500)
window.config(bg="#111")


# File Path Handling 
# You should make image in the same folder of main.py
fileName="calculator.ico"
currentRunningPyFile = __file__
toRemoveFromPath = os.path.basename(__file__)
lenghtOfRunningFile = len(toRemoveFromPath)
lengthOfCompletePath = len(currentRunningPyFile)
currentRunningPyFile = currentRunningPyFile[:lengthOfCompletePath-lenghtOfRunningFile]
fileName = currentRunningPyFile+fileName
window.iconbitmap(fileName)


# Label one + Check box one
label1=tkinter.Label(text="Enter your First Number")
label1.pack()
label1.place(relx = 0.5,rely = 0.1,anchor="center",width=200)
checkBox1=tkinter.Entry()
checkBox1.pack()
checkBox1.place(relx = 0.5,rely = 0.2,anchor="center",width=200)


# Operation + checkBox2
label2=tkinter.Label(text="Enter Operation: + - * / ")
label2.pack()
label2.place(relx = 0.5,rely = 0.35,anchor="center",width=200)
checkBox2=tkinter.Entry()
checkBox2.pack()
checkBox2.place(relx = 0.5,rely = 0.45,anchor="center",width=200)


# Label one + Check box one
label3=tkinter.Label(text="Enter Your Second Number")
label3.pack()
label3.place(relx = 0.5,rely = 0.6,anchor="center",width=200)
checkBox3=tkinter.Entry()
checkBox3.pack()
checkBox3.place(relx = 0.5,rely = 0.7,anchor="center",width=200)


# Result
def calculate():

    try:

        operation=checkBox2.get()
        if operation  in "+/-*" and len(operation)!=0:
            num1=int(checkBox1.get())
            num2=int(checkBox3.get())
            res=0
            if operation=="+":
                res=num1+num2
            elif operation=="-":
                res=num1-num2
            elif operation=="*":
                res=num1*num2
            elif operation=="/":
                res=num1/num2
                res="{:.3f}".format(res)
            result=tkinter.Label(text=f"The Result is {res}")
            result.pack()
            result.place(relx=.5,rely=.9,anchor="center",width=200)
        else:

            tkinter.messagebox.showerror("Error","You Must Enter only one of these Operation : + - / * ")

    except Exception as ep:

        tkinter.messagebox.showerror('error', "Add First Number and Second Number and Try again")


btn=tkinter.Button(text="Calculate",command=calculate,bg='#227C70')   
btn.pack()
btn.place(relx=.5,rely=.8,anchor="center",width=100)



window.mainloop()