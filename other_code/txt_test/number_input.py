import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

def callbackFunc(landString,resultString):
    if landString.get() == "" :resultString.set("請輸入學號.....")
    else:
        resultString.set("輸入成功.....")
        #print(landString.get())
        bbb=[]
        ccc=''
        f = open('file_io.txt','r')
        k = f.readlines()
        f.close()
        a=k[0].split(',')

        for i in range(len(a)):
            bbb.append(a[i])

        f = open('file_io.txt', 'w')
        bbb.append(landString.get())

        for i in range(len(bbb)):
            if i == len(bbb)-1:ccc=ccc+bbb[i]
            else:ccc=ccc+bbb[i]+','
        #print(ccc)
        f.write(ccc)
        f.close() 
        quit() 
def main():
    app = tk.Tk() 
    w=450
    h=100
    ws = app.winfo_screenwidth()
    hs = app.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    app.geometry('%dx%d+%d+%d' % (w, h, x, y))
    fontStyle = tkFont.Font(family="Lucida Grande", size=20)
    labelLand = tk.Label(app,text = "請輸入學號",font=fontStyle)
    labelLand.grid(column=0, row=0, sticky=tk.W)


    landString = tk.StringVar()

    entryLand = tk.Entry(app, width=20,font=fontStyle, textvariable=landString)
    entryLand.grid(column=1, row=0, padx=10)


    resultButton = tk.Button(app, text = '確定',font=fontStyle,command=lambda:callbackFunc(landString,resultString))
    resultButton.grid(column=0, row=2, pady=10, sticky=tk.W)

    resultString=tk.StringVar()
    resultLabel = tk.Label(app,font=fontStyle, textvariable=resultString)
    resultLabel.grid(column=1, row=2, padx=10, sticky=tk.W)

    app.mainloop()


if __name__ == '__main__':
    main()