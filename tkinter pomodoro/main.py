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
time = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(time)
    timer.config(text="Timer", fg=RED)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps 
    reps += 1
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer.config(text="Long Break", fg=RED)
        count_down(long_break_time)
    elif reps % 2 == 0:
        timer.config(text="Break", fg=PINK)
        count_down(short_break_time)
    else:
        timer.config(text="Work", fg=GREEN)
        count_down(work_time)
 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60 
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global time
        time = window.after(1000, count_down, count -1)
    else:
        mark = ""
        for i in range(math.floor(reps/2)):
            mark += "✓"
        check_mark.config(text=mark)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



#Text
timer = Label(window, text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
timer.grid(row=0, column=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Buttons
start = Button(text="Start", highlightthickness=0, bg=YELLOW, borderwidth=0, highlightbackground=YELLOW, command=start_timer)
start.grid(column=0, row=2)
reset = Button(text="Reset", highlightthickness=0, bg=YELLOW, borderwidth=0, highlightbackground=YELLOW, command=reset_timer)
reset.grid(column=2, row=2)

check_mark = Label()


check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)

window.mainloop()