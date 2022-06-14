# Import all necessary modules
from tkinter import *
# Importing datetime and giving it the alias dt
import datetime as dt
# Giving time an alias of t
import time as t
# Importing windsound as winsnd
import winsound as winsnd

""" Creating a function named alarm() 
feed in the argument set_alarm_timer
contains a while loop with a boolean that's true 
a while loop will process until it's condition is false."""

           # Arugment
def alarm(set_alarm_timer):
    while True:
        t.sleep(1)
        # Group member takes the argument of our internal computers current time
        current_time = dt.datetime.now()
        # Takes the current_time member and passes a converstion via strftime and formats the time
        now = current_time.strftime("%H:%M:%S")
        # Member that adds the date to the current_time member and the string formats a date
        date = current_time.strftime("%d/%m/%Y")
        # Printing in log to make sure it works
        print("The Set Date is:", date)
        print(now)
        # Conditional statement that initiates if conditions are met; if it matches with the while loop
        if now == set_alarm_timer:
            print("Get Up!")
        winsnd.PlaySound("sound.wav",winsnd.SND_ASYNC)
        break

# Another function that gets user value for setting the alarm
def actual_time():
    # Sets it in a string format via f-string
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    # If user input time matches set_alarm_timer arument it initiates the alarm
    alarm(set_alarm_timer)

# Creating a GUI using tkinter Tk() creates app
clock = Tk()
# Title of app
clock.title("Alarm Clock")
# Dimensions of our tkinter window
clock.geometry("400x200")
time_format = Label(clock, text = "Enter Time in 24 Military Time",
fg = "red", bg = "black", font = "Roboto").place(x = 60, y = 120)
addTime = Label(clock,text = "What Time Would You Like To Wake Up?",
fg = "blue", relief = "solid", font = ("Helvetica", 7, "bold")).place(x = 0, y = 29)

# Variables we need to initalize the alarm reason why we use StringVar is because we formatted the string already
hour = StringVar()
min = StringVar()
sec = StringVar()

# Time required to set the alarm clock
hourTime = Entry(clock, textvariable = hour, bg = "pink", width = 15).place(x = 110, y = 30)
minTime = Entry(clock, textvariable = min, bg = "pink", width = 15).place(x = 150, y = 30)
secTime = Entry(clock, textvariable = sec, bg = "pink", width = 15).place(x = 200, y = 30)

# To take time input by user
submit = Button(clock, text = "Set Alarm", fg = "red", width = 10, command = actual_time) .place(x = 110, y = 70)

# Execution of the window
clock.mainloop()