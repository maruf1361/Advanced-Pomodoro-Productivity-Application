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
timer_countdown = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer_countdown)
    canvas.itemconfig(canvas_timer, text = "00:00")
    timer.config(text="Timer")
    tick_label.config(bg= YELLOW, fg= GREEN, font=(12))
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN*60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        count_down(short_break_secs)
        timer.config(text="Break", fg= PINK)
    elif reps % 8 == 0:
        count_down(long_break_secs)
        timer.config(text="Break", fg = RED)
    else:
        count_down(work_secs)
        timer.config(text = "Work", fg = GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count/60)
    seconds = count%60
    if seconds == 0:
        seconds = "00"
    elif seconds in range(10):
        new_seconds = str(0) + str(seconds)
        seconds = new_seconds

    canvas.itemconfig(canvas_timer, text = f"{minutes}:{seconds}")

    if count > 0:
        global timer_countdown
        timer_countdown = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✔"
        tick_label.config(text= marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg= YELLOW)


timer = Label(text= "Timer", font=(FONT_NAME, 40, "bold"))
timer.config(bg= YELLOW, fg= GREEN)
timer.grid(row= 0, column=1)

canvas = Canvas(width= 200, height= 224, bg= YELLOW, highlightthickness= 0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = img)
canvas_timer = canvas.create_text(100, 130, text="00:00", fill= "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column= 1)

start_btn = Button(text="Start", command= start_timer)
start_btn.config(padx=10, highlightthickness= 0)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", command= reset_timer)
reset_btn.config(padx=10, highlightthickness= 0)
reset_btn.grid(row=2, column=2)

tick_label = Label(bg= YELLOW, fg= GREEN, font=(12))
tick_label.grid(row= 3, column= 1)




window.mainloop()