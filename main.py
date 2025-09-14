import tkinter as tk
from time import strftime
from datetime import date
from tkinter import messagebox
import random
import platform


# برای صدا
try:
    from playsound import playsound
    SOUND_ENABLED = True
except ImportError:
    import winsound
    SOUND_ENABLED = False


root = tk.Tk()
root.title("Digital Clock with Alarm")
root.geometry("500x320")
root.config(bg="black")


# --- رنگ ها --
colors = ["red", "green", "blue", "yellow", "cyan", "orange", "lime", "magenta"]


# --- ساعت ---
def time():
    string = strftime("%H:%M:%S")
    label_time.config(text=string, fg=random.choice(colors))
    
    # بررسی آلارم
    if alarm_time.get() == string[:5]:
        trigger_alarm()
       

    label_time.after(1000, time)


#  --- تاریخ ---
today = date.today()
label_date = tk.Label(root, text=today.strftime("%d %B %Y"),
                      font=("Arial", 18, "bold"), bg="black", fg="cyan")
label_date.pack(pady=10)

# --- نمایش ساعت ---
label_time = tk.Label(root, font=("Arial", 48, "bold"), bg="black", fg="lime")
label_time.pack(pady=20)


# --- ALARM ---
frame_alarm = tk.Frame(root, bg="black")
frame_alarm.pack(pady=10)

tk.Label(frame_alarm,text="Set Alarm (HH:MM)",font=("Arial",14),fg="white",bg="black").pack(side="left")


alarm_time = tk.StringVar()

entry_time =tk.Entry(frame_alarm, textvariable=alarm_time,font=("Arial",14),width=7 )
entry_time.pack(side="left",padx=10)


# --- Buttom ---
def set_alarm():
    if alarm_time.get():
        messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time.get()}")
    else:
        messagebox.showwarning("Alarm","Enter a Valid time !")


tk.Button(frame_alarm, text="set", font=("Arial", 12 , "bold"),
          command=set_alarm,bg="green",fg="black").pack(side="left")


# --- اجرای آلارم ---
def trigger_alarm():
    messagebox.showinfo("🕰️ Alarm", f"It`s {alarm_time.get()} ! ⏰ ")
    # پخش صدا
    try:
        if SOUND_ENABLED:
            playsound("alarm.wav")   # باید یک فایل alarm.mp3 کنار کد بذاری
        else:
            winsound.Beep(1000, 1000)  # بوق ساده در ویندوز
    except Exception as e:
        print("Sound error:", e)

    alarm_time.set("")  # بعد از آلارم خالی می‌کنه


time()
root.mainloop()
