from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    #timer 00:00
    #title : Timer
    #reset check mark
    canvas.itemconfig(timer_count,text="00:00")
    timer_text.config(text="Timer", fg=GREEN)
    green_mark.config(text="")
    global reps
    reps=0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_text.config(text="Break", fg=RED)
    elif reps % 2 == 0 :
        countdown(short_break_sec)
        timer_text.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        timer_text.config(text="Work", fg=GREEN)

# def start_timer():
#     countdown(11)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_count, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks =""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✔"
        green_mark.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO APP ")
window.config(padx=100, pady=50, background=YELLOW)




#Image + counter
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_count = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35, "bold"))
canvas.grid(row=1, column=1)




#Timer text
timer_text = Label(text="Timer",fg=GREEN, bg=YELLOW,  font=(FONT_NAME, 50))
timer_text.grid(row=0, column=1)



#Start button
start_button = Button(text="Start", font=FONT_NAME, bg="white", command=start_timer)
start_button.grid(column=0, row=2)

#Reset button
reset_button = Button(text="Reset", font=FONT_NAME, bg="white", command=reset_timer)
reset_button.grid(column=2, row=2)

#green_mark
green_mark = Label( fg=GREEN, bg=YELLOW, font=(30))
green_mark.grid(row=3, column=1)


#using fg => for label and other instead of bg
#text  ="✔"
#use grid





window.mainloop()


