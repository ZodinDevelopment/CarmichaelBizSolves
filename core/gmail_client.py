import smtplib


def setup_gmail(msg, password, testing=True):

    sender = 'garrettdylan0702@gmail.com'
    receiver = 'carmichaelbusinesssolutions@gmail.com'
    test_receiver = 'toasterkief@protonmail.com'

    gmail_client = smtplib.SMTP('smtp.gmail.com', 587)
    gmail_client.ehlo()
    gmail_client.starttls()
    gmail_client.ehlo
    
    gmail_client.login(sender, password)

    if testing:
        gmail_client.sendmail(sender, test_receiver, msg)

        print('Sent to dev mailbox at {}'.format(test_receiver))

    else:
        gmail_client.sendmail(sender, receiver, msg)

        print('Sent to service subscriber at {}'.format(receiver))
        gmail_client.sendmail(sender, test_receiver, msg)
    

        print('Copy sent to dev mailbox at {} for debug and maintenance purposes.'.format(test_receiver))

    gmail_client.close()


