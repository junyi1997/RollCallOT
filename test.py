# -*- coding: utf-8 -*-
import tkinter as tk
#import tkinter.font as tkFont
import tkinter.messagebox
#import face_reco_from_camera_ot_single_person
#import features_extraction_to_csv
#import get_faces_from_camera    

def New_person():
    #get_faces_from_camera.main()
    pass

def update():
    print("開始更新")
    #features_extraction_to_csv.main()
    #pass
    print("更新成功")

def fd():
    #face_reco_from_camera_ot_single_person.main()
    pass

root=tk.Tk()
root.title("人臉辨識系統")
root.geometry("1000x800+0+0")
#fontStyle = tkFont.Font(family="Lucida Grande", size=20)   ,font=fontStyle

btn0=tk.Label(root,text="點名系統", height=5,bg='yellow',font= ('Noto Sans Mono CJK TC Regular',30)).pack(side='top', fill='x')
btn1=tk.Button(root,text="新增照片", width=20,bg='light green',font= ('Noto Sans Mono CJK TC Regular',30),command=lambda:New_person()).pack(side='left', fill='y')
btn2=tk.Button(root,text="更新", width=20,bg='deep sky blue',font= ('Noto Sans Mono CJK TC Regular',30),command=lambda:update()).pack(side='left', fill='y')
btn3=tk.Button(root,text="人臉辨識", width=20,bg='hot pink',font= ('Noto Sans Mono CJK TC Regular',30),command=lambda:fd()).pack(side='left', fill='y')


root.mainloop()
