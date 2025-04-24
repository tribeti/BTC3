import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time
from dotenv import load_dotenv
import os
from pathlib import Path
import shutil

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
PASSWORD = os.getenv("PASSWORD")
RECIEVER_EMAIL = os.getenv("RECIEVER_EMAIL")

file = Path("sql\\a.sql")

def main():
    if not file.exists():
        text = "Khong tim thay file backup"
    else:
        try:
            shutil.copyfile(file, "backup\\a.sql")
            text = "Backup thanh cong"
        except Exception as e:
            text = f"Backup that bai: {e}"
        
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = RECIEVER_EMAIL
    message['Subject'] = "Ket qua backup database"
    message.attach(MIMEText(text,'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com',587)

        server.starttls()
        server.login(SENDER_EMAIL,PASSWORD)

        text = message.as_string()
        server.sendmail(SENDER_EMAIL,RECIEVER_EMAIL,text)

        print(f"da gui den {RECIEVER_EMAIL}")
        server.quit()
    except Exception as e:
        print(f"loi {e}")

schedule.every().day.at("00:00").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)