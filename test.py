# -*- coding: utf-8 -*-
import tkinter as tk
#import tkinter.font as tkFont
import tkinter.messagebox
import face_reco_from_camera_ot_single_person
import features_extraction_to_csv
import get_faces_from_camera    

def New_person():
    get_faces_from_camera.main(screenwidth,screenheight)
    #pass

def update():
    print("開始更新")
    features_extraction_to_csv.main()
    #pass
    print("更新成功")

def fd():
    face_reco_from_camera_ot_single_person.main(screenwidth,screenheight)
    #pass

root=tk.Tk()
root.title("人臉辨識系統")


#fontStyle = tkFont.Font(family="Lucida Grande", size=20)   ,font=fontStyle
width=475
height=300
screenwidth = root.winfo_screenwidth()  
screenheight = root.winfo_screenheight()  
size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2) 
root.geometry(size)
btn0=tk.Label(root,text="點名系統", height=3,bg='yellow',font= ('Noto Sans Mono CJK TC Regular',20)).pack(side='top', fill='x')
btn1=tk.Button(root,text="新增照片", width=8,bg='light green',font= ('Noto Sans Mono CJK TC Regular',20),command=lambda:New_person()).pack(side='left', fill='y')
btn2=tk.Button(root,text="更新", width=8,bg='deep sky blue',font= ('Noto Sans Mono CJK TC Regular',20),command=lambda:update()).pack(side='left', fill='y')
btn3=tk.Button(root,text="人臉辨識", width=8,bg='hot pink',font= ('Noto Sans Mono CJK TC Regular',20),command=lambda:fd()).pack(side='left', fill='y')


root.mainloop()
