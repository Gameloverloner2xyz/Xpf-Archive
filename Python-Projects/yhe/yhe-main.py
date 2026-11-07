print("The world's one and only Tame Impala virus")

from tkinter import *
from tkinter import ttk
from PIL import Image as PILImage
from PIL import ImageTk
import time


#Opening
#Corrected?windows
#Outdated?functions
#Outdated?StillWorking?IMPORTANT NOTE: The windows for the opening are created from the bottom up, the first lyric being the first window created, the second being in the first function, so on and so forth
#IMPORTANT NOTE: The other windows are just for the opening go to the eighth window for most of the actual content
#NotThatImportant?KEYWORD:'SOME'?Note: I forget at what point but somewhere throughout the code I stopped changing some of the names accordingly so have fun with that
def button_close1F():
    #second window
    def button_close2F():
        #third window
        def button_close3F():
            #fourth window
            def button_close4F():
                #fifth window
                def button_close5F():
                    #sixth window
                    def button_close6F():
                        #seventh window
                        def button_close7F():
                            #eight-main window
                            window6.destroy()
                            window7 = Tk()
                            window7.geometry("500x500")
                            window7.title("yhe")
                            window7.config(background="#94C6D4")
                            window7.config()
                            style = ttk.Style()
                            style.theme_use("classic")
                            style.configure('Windows.TButton',
                                            font=('Courier', 12),
                                            background='#94C6D4',
                                            foreground='black',
                                            borderwidth=1,
                                            relief='flat')

                            window7.mainloop()
                        window5.destroy()
                        window6 = Tk()
                        window6.geometry("300x200")
                        window6.title("yhe")
                        window6.config(background="#94C6D4")
                        window6.config()
                        style = ttk.Style()
                        style.theme_use("classic")
                        style.configure('Windows.TButton',
                                        font=('Courier', 12),
                                        background='#94C6D4',
                                        foreground='black',
                                        borderwidth=1,
                                        relief='flat')
                        style.map('Custom.TButton',
                                  background=[('pressed', '#DE0000'), ('active', '#004ADE')])


                        spider_face_pil4 = PILImage.open("images/spideyface.png")
                        spider_faceR4 = spider_face_pil4.resize((25, 25))
                        spider_faceRTK4 = ImageTk.PhotoImage(spider_faceR4)

                        ti1 = Label(window6, text=" tryna figure this whole mess out", font="Courier", bg="#94C6D4",
                                    image=spider_faceRTK4, compound="left")
                        ti1.place(x=5, y=80)
                        button_close3 = ttk.Button(window6, text='Close', style='Custom.TButton')
                        button_close3.config(command=button_close7F)
                        button_close3.place(x=70, y=120)

                        window6.mainloop()

                    window4.destroy()
                    window5 = Tk()
                    window5.geometry("300x200")
                    window5.title("yhe")
                    window5.config(background="#94C6D4")
                    window5.config()
                    style = ttk.Style()
                    style.theme_use("classic")
                    style.configure('Windows.TButton',
                                    font=('Courier', 12),
                                    background='#94C6D4',
                                    foreground='black',
                                    borderwidth=1,
                                    relief='flat')

                    style.map('Custom.TButton',
                              background=[('pressed', '#DE0000'), ('active', '#004ADE')])

                    spider_legs_pil4 = PILImage.open("images/spiderlegs.png")
                    spider_legsR4 = spider_legs_pil4.resize((25, 25))
                    spider_legsRTK4 = ImageTk.PhotoImage(spider_legsR4)

                    ti1 = Label(window5, text="   i'm a tragedy", font="Courier", bg="#94C6D4", image=spider_legsRTK4,
                                compound="left")
                    ti1.place(x=15, y=80)
                    button_close3 = ttk.Button(window5, text='Close', style='Custom.TButton')
                    button_close3.config(command=button_close6F)
                    button_close3.place(x=70, y=120)

                    window5.mainloop()

                window3.destroy()
                window4 = Tk()
                window4.geometry("300x200")
                window4.title("yhe")
                window4.config(background="#94C6D4")
                window4.config()
                style = ttk.Style()
                style.theme_use("classic")
                style.configure('Windows.TButton',
                                font=('Courier', 12),
                                background='#94C6D4',
                                foreground='black',
                                borderwidth=1,
                                relief='flat')

                style.map('Custom.TButton',
                          background=[('pressed', '#DE0000'), ('active', '#004ADE')])

                spider_face_pil4 = PILImage.open("images/spideyface.png")
                spider_faceR4 = spider_face_pil4.resize((25, 25))
                spider_faceRTK4 = ImageTk.PhotoImage(spider_faceR4)

                ti1 = Label(window4, text=" do you wanna tear my heart out?", font="Courier", bg="#94C6D4",
                            image=spider_faceRTK4, compound="left")
                ti1.place(x=15, y=80)
                button_close3 = ttk.Button(window4, text='Close', style='Custom.TButton')
                button_close3.config(command=button_close5F)
                button_close3.place(x=70, y=120)

                window4.mainloop()

            window2.destroy()
            window3=Tk()
            window3.geometry("300x200")
            window3.title("yhe")
            window3.config(background="#94C6D4")
            window3.config()
            style = ttk.Style()
            style.theme_use("classic")
            style.configure('Windows.TButton',
                            font=('Courier', 12),
                            background='#94C6D4',
                            foreground='black',
                            borderwidth=1,
                            relief='flat')

            style.map('Custom.TButton',
                      background=[('pressed', '#DE0000'), ('active', '#004ADE')])

            spider_legs_pil3 = PILImage.open("images/spiderlegs.png")
            spider_legsR3 = spider_legs_pil3.resize((25, 25))
            spider_legsRTK3 = ImageTk.PhotoImage(spider_legsR3)

            ti4 = Label(window3, text="   babe (babe)", font="Courier", bg="#94C6D4", image=spider_legsRTK3, compound="left")
            ti4.place(x=45, y=80)
            button_close3 = ttk.Button(window3, text='Close', style='Custom.TButton')
            button_close3.config(command=button_close4F)
            button_close3.place(x=70, y=120)

            window3.mainloop()

        window1.destroy()
        window2=Tk()
        window2.geometry("300x200")
        window2.title("yhe")
        window2.config(background="#94C6D4")
        window2.config()
        style = ttk.Style()
        style.theme_use("classic")
        style.configure('Windows.TButton',
                        font=('Courier', 12),
                        background='#94C6D4',
                        foreground='black',
                        borderwidth=1,
                        relief='flat')

        style.map('Custom.TButton',
                  background=[('pressed', '#DE0000'), ('active', '#004ADE')])

        spider_face_pil2 = PILImage.open("images/spideyface.png")
        spider_faceR2 = spider_face_pil2.resize((25, 25))
        spider_faceRTK2 = ImageTk.PhotoImage(spider_faceR2)

        button_close2 = ttk.Button(window2, text='Close', style='Custom.TButton')
        button_close2.config(command=button_close3F)
        button_close2.place(x=70, y=120)

        ti3 = Label(window2, text="   i'm a loser,", font="Courier", bg="#94C6D4", image=spider_faceRTK2, compound="left")
        ti3.place(x=45, y=80)
        window2.mainloop()


    window.destroy()
    window1 = Tk()
    window1.geometry("300x200")
    window1.title("yhe")
    window1.config(background="#94C6D4")
    window1.config()
    style = ttk.Style()
    style.theme_use("classic")
    style.configure('Windows.TButton',
                    font=('Courier', 12),
                    background='#94C6D4',
                    foreground='black',
                    borderwidth=1,
                    relief='flat')

    style.map('Custom.TButton',
              background=[('pressed', '#DE0000'), ('active', '#004ADE')])

    spider_legs_pil1 = PILImage.open("images/spiderlegs.png")
    spider_legsR1 = spider_legs_pil1.resize((25, 25))
    spider_legsRTK1 = ImageTk.PhotoImage(spider_legsR1)
    ti2 = Label(window1, text="   you couldn't write this (ah)", font="Courier", bg="#94C6D4", image=spider_legsRTK1,
                compound="left")
    ti2.image=spider_legsRTK1
    ti2.place(x=10, y=80)
    button_close2 = ttk.Button(window1, text='Close', style='Custom.TButton')
    button_close2.config(command=button_close2F)
    button_close2.place(x=70, y=120)

    window1.mainloop()

window = Tk()
window.geometry("300x200")
window.title("yhe")
window.config(background="#94C6D4")
window.config()
style = ttk.Style()
style.theme_use("classic")
style.configure('Windows.TButton',
                font=('Courier', 12),
                background='#94C6D4',
                foreground='black',
                borderwidth=1,
                relief='flat')
style.map('Custom.TButton',
          background=[('pressed', '#DE0000'), ('active', '#004ADE')])
#images
spider_face_pil = PILImage.open("images/spideyface.png")
spider_faceR=spider_face_pil.resize((25, 25))
spider_faceRTK = ImageTk.PhotoImage(spider_faceR)

spider_legs_pil = PILImage.open("images/spiderlegs.png")
spider_legsR=spider_legs_pil.resize((25, 25))
spider_legsRTK = ImageTk.PhotoImage(spider_legsR)

#opening for main window
ti=Label(window, text="Loser - Tame Impala",  font="Courier", bg="#94C6D4", fg="#4300DE")
ti.pack()
ti1 = Label(window,text="  that's how my life is", font="Courier", bg="#94C6D4", image=spider_faceRTK,compound="left")
ti1.place(x=40, y=80)
button_close1=ttk.Button(window, text='Close', style='Custom.TButton')
button_close1.config(command=button_close1F)
button_close1.place(x=70, y=120)

window.mainloop()