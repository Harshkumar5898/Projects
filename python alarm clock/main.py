import datetime

import pygame

from tkinter import *


if __name__ == '__main__':

    root = Tk()

    def play(stopper="stop"):

        pygame.init()
        pygame.mixer.music.load("After_dark.mp3")
        pygame.mixer.music.play()

        while True:

            a = input("Enter stop to stop alarm")
            if a == stopper:

                mixer.music.stop()

                break

    def time():
        time = f"{hour.get()}:{minute.get()}"
        alarm(time)

    def alarm(time):
        current_time = datetime.datetime.now().strftime("%H:%M")

        while True:
            if time == current_time:
                play()
                break

    root.geometry("300x200")

    label = Label(root, text="Enter Time", font=("Helvetica 20 bold"))
    label.pack()

    hour = StringVar()
    hour_input = Entry(root, width=2, textvariable=hour,
                       bg="pink", font=('Arial 24')).place(x=80, y=70)

    minute = StringVar()
    minute_input = Entry(root, width=2, textvariable=minute,
                         bg="pink", font=('Arial 24')).place(x=165, y=70)

    button_set = Button(root, text="SET", command=time).place(x=137, y=130)

    root.mainloop()
