from customtkinter import * 
from exersices.push_up import PushUp
from exersices.dumble import Dumble
from exersices.squad import Squad




windows = CTk(fg_color="#e6eefc")
windows.title("AI Exercise")
windows.maxsize(350,420)
windows.minsize(350,420)
windows.config(background = "#e6eefc")

myfont = CTkFont("vazir" ,25)
f1 = CTkFrame(windows , fg_color="#e6eefc")
f2 = CTkFrame(windows , fg_color="#e6eefc")

f1.place(x=50 ,y=85)
f2.place(x=35 , y=140)

def pushup():
    windows.destroy()
    PushUp()

def arm():
    windows.destroy()
    Dumble()


def squad():
    windows.destroy()
    Squad()



Text_label = CTkLabel(f1 , text=": ورزش مورد نظر خود را وارد کنید " ,
                       font= CTkFont("vazir" , 20) ,
                         text_color="black")
Text_label.pack()

pushup_button = CTkButton(f2 , text="شنا سوئدی" ,
                           command=pushup ,
                             font=myfont ,
                               fg_color="#468bfa" ,
                                 hover_color="#0b5fe6" ,
                                   corner_radius=5 ,
                                     width=280 , height=38)
pushup_button.pack()

arm_button = CTkButton(f2 , text="جلو بازو با دمبل" ,
                        command=arm ,
                          font=myfont ,
                            fg_color="#468bfa" ,
                              hover_color="#0b5fe6" ,
                                corner_radius=5 ,
                                  width=280 , height=38)
arm_button.pack(pady=20)

squad_button = CTkButton(f2 , text="اسکوات" ,
                          command=squad ,
                            font= myfont ,
                              fg_color="#468bfa" ,
                                hover_color="#0b5fe6" ,
                                  corner_radius=5 ,
                                    width=280 , height=38 )
squad_button.pack()

windows.mainloop()