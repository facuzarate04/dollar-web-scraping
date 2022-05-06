import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

class Notify:
    def prepare_mail_notification():
        """with open(textfile, 'rb') as fp:
        msg = MIMEText(fp.read())
        msg['From'] = sender
        msg['To'] = to
        msg['Subject'] = 'The contents of %s' % textfile
        """
        sender = os.getenv("MAIL_FROM")
        to = os.getenv("MAIL_TO")
        password = os.getenv("MAIL_PASSWORD")
        msg = "Cuerpo del mensaje"

        return sender, to, password, msg

    def send_mail_notification():
        sender, to, password, msg = Notify.prepare_mail_notification()

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender=sender, password=password)
        server.sendmail(sender=sender, to=to, msg=msg)
        server.quit()
        pass
        