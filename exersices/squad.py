import os
import cv2
import cvzone.PoseModule
from customtkinter import * 
from PIL import Image, ImageTk
from exersices.DataManager.DataManager import SaveData

def Squad():
    global nowrep

    window = CTk()
    window.title("سکوات")
    window.config(background="#e6eefc")
    window.maxsize(640,480)
    window.minsize(640,480)

    camera_frame = CTkFrame(window ,bg_color="#e6eefc" , fg_color="#e6eefc")
    texts_frame = CTkFrame(window , bg_color="#e6eefc" , fg_color="#e6eefc")
    column1_frame = CTkFrame(texts_frame , bg_color="#e6eefc" , fg_color="#e6eefc")
    column2_frame = CTkFrame(texts_frame , bg_color="#e6eefc" , fg_color="#e6eefc")
    column3_frame = CTkFrame(texts_frame , bg_color="#e6eefc" , fg_color="#e6eefc")

    camera_frame.pack()
    texts_frame.pack()
    column1_frame.grid(row=0 , column=0)
    column2_frame.grid(row=0 , column=1 , padx=50)
    column3_frame.grid(row=0 , column=2)


    camera = cv2.VideoCapture(0)
    detector = cvzone.PoseModule.PoseDetector()

    data = SaveData("Squad")
    nowrep = 0
    maxrep = data.maxrep
    lastrep = data.lastrep
    filter = [0]

    MyFont = CTkFont("Comic Sans MS" , 35)
    frame_label = CTkLabel(camera_frame , text="" , fg_color="#9cbfff" , corner_radius=8)
    frame_label.pack(pady=10)

    def predict(frame) :
        global nowrep

        frame = detector.findPose(frame , draw=False)
        points = detector.findPosition(frame , draw= False)[0]
        
        if points:
            right_leg = [points[24][:-1] , points[26][:-1] , points[28][:-1]]
            left_leg = [points[23][:-1] , points[25][:-1] , points[27][:-1]]

            right_angle = int(detector.findAngle(right_leg[0] , right_leg[1] , right_leg[2] , frame , color=(156 , 191 , 255))[0])
            left_angle = int(detector.findAngle(left_leg[0] , left_leg[1] , left_leg[2] , frame , color=(156 , 191 , 255))[0])

            # normalrize the hands angles
            if right_angle > 180 :
                right_angle = abs(360 - right_angle) 
            if left_angle > 180 :
                left_angle = abs(360 - left_angle) 

            angle = (left_angle + right_angle)/2

            if angle < 80 and filter[0] == 0 :
                nowrep += 1 
                filter[0] = 1
            elif angle > 80 and filter[0] == 1 :
                filter[0] = 0 



        frame = cv2.resize(frame , (460 ,280))
        return frame

    

    def show_frame():
        _ , frame = camera.read()
        if _ :
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = predict(frame=frame)
            frame = Image.fromarray(frame)
            frame = ImageTk.PhotoImage(image=frame)
            frame_label.img = frame
            frame_label.configure(image=frame)
            nowrep_text.configure(text=nowrep)
        else :
            frame_label.configure(text="the camera is not find !!!" , font=MyFont)
        frame_label.after(10, show_frame)


    def clear():
        global nowrep
        data.update_csv(nowrep=nowrep)
        nowrep = 0 
        lastrep = data.lastrep
        maxrep = data.maxrep

        nowrep_text.configure(text=nowrep)
        lastrep_text.configure(text=lastrep)
        maxrep_text.configure(text=maxrep)



    lastrep_text_title = CTkLabel(column1_frame , text="Last Rep :" , text_color="#9cbfff" , font = MyFont)
    lastrep_text_title.pack(pady=5)

    lastrep_text = CTkLabel(column1_frame , text=lastrep , text_color="#9cbfff" , font = MyFont)
    lastrep_text.pack()

    nowrep_text_title = CTkLabel(column2_frame , text="Now Rep :" , text_color="#9cbfff" , font = CTkFont("Comic Sans MS" , 30))
    nowrep_text_title.pack(pady=3)

    nowrep_text = CTkLabel(column2_frame , text=nowrep , text_color="#9cbfff" , font = CTkFont("Comic Sans MS" , 30))
    nowrep_text.pack()

    clear_button = CTkButton(column2_frame , 
                            text="Clear" ,
                            font=CTkFont("vazir" , 25) , 
                            command=clear , 
                            fg_color="#468bfa" ,
                            hover_color="#0b5fe6" ,
                            corner_radius=8 ,
                            width=150 , height=45
                            )
    clear_button.pack(pady=10)


    maxrep_text_title = CTkLabel(column3_frame , text="Max Rep :" , text_color="#9cbfff" , font=MyFont)
    maxrep_text_title.pack(pady=5)

    maxrep_text = CTkLabel(column3_frame , text=maxrep , text_color="#9cbfff" , font=MyFont)
    maxrep_text.pack()

    show_frame()
    window.mainloop()
    data.update_csv(nowrep=nowrep)
