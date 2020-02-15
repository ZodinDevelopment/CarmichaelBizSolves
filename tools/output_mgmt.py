import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


FROM = 'garretdylan0702@gmail.com'
TO = ['carmichaelbusinesssolutions@gmail.com', 'toasterkief@protonmail.com']
SUBJECT = 'New Members'


def send_report(dev_pass, testing):
    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT
    msg['From'] = FROM
    msg['To'] = ', '.join(TO)
    
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("new_users.txt", "rb").read())
    encoders.encode_base64(part)
    
    part.add_header('Content-Disposition', 'attachment; filename="new_users.txt"')
    
    msg.attach(part)
    
    gmail_client = smtplib.SMTP('smtp.gmail.com', 587)
    gmail_client.ehlo()
    gmail_client.starttls()
    gmail_client.ehlo
    
    gmail_client.login(FROM, dev_pass)
    
    if testing:
        pass
    
    else:
        gmail_client.sendmail(FROM, TO, msg.as_string())
        
    print('Report delivered successfully.')
    
def make_dev_log(message, delivered_at):
    with open('dev.log', 'a') as f:
        f.write('|===========================\n')
        f.write(' Report delivered to client at {}\n\n'.format(delivered_at.ctime()))
        f.write('Copy of report:\n\n\n')
        f.write(message)
        f.write('\n===============================\n\n')
        
    print('Log file updated with today\'s runtime results.')
    
    
