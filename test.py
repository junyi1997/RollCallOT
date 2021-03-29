import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
import face_reco_from_camera_ot_single_person
import features_extraction_to_csv
import get_faces_from_camera    

def New_person():
    get_faces_from_camera.main()

def update():
    print("開始更新")
    features_extraction_to_csv.main()
    print("更新成功")

def fd():
    face_reco_from_camera_ot_single_person.main()

root=tk.Tk()
root.title("人臉辨識系統")
root.geometry("870x600+200+200")
fontStyle = tkFont.Font(family="標楷體", size=20)

btn0=tk.Label(root,text="點名系統", height=5,bg='yellow',font=fontStyle).pack(side='top', fill='x')
btn1=tk.Button(root,text="新增照片", width=20,bg='light green',font=fontStyle,command=lambda:New_person()).pack(side='left', fill='y')
btn2=tk.Button(root,text="更新", width=20,bg='deep sky blue', font=fontStyle,command=lambda:update()).pack(side='left', fill='y')
btn3=tk.Button(root,text="人臉辨識", width=20,bg='hot pink',font=fontStyle,command=lambda:fd()).pack(side='left', fill='y')


root.mainloop()
