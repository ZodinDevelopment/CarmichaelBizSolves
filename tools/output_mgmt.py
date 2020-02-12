import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders 


EMAIL_FROM = 'garrettdylan0702@gmail.com'
EMAIL_TO = 'carmichaelbusinesssolutions@gmail.com'
DEV_EMAIL = 'toasterkief@protonmail.com'


def send_report(dev_pass, testing):
    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT
    msg['From'] = EMAIL_FROM
    msg['To'] = ', '.join(EMAIL_TO)
    
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("new_users.txt", "rb").read())
    encoders.encode_base64(part)


    part.add_header('Content-Disposition', 'attachment; filename="new_users.txt"')

    msg.attach(part)

    gmail_client = smtplib.SMTP('smtp.gmail.com', 587)
    gmail_client.ehlo()
    gmail_client.starttls()
    gmail_client.ehlo

    gmail_client.login(EMAIL_FROM, dev_pass)

    if testing:
        pass

    else:
        gmail_client.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())


    print('Sendmail successful.')

def make_dev_log(message, delivered_at):
    with open('dev.log', 'a') as f:
        f.write('|_____________________\n')
        f.write(' Report delivered to client at {}\n\n'.format(delivered_at.ctime()))
        f.write('Copy of Report:\n\n\n')
        f.write(message)
        f.write('\n==============================\n\n')

    print('Log file updated with today\'s runtime results.')

     
