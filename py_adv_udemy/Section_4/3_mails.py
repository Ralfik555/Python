import smtplib
import functools

mailFrom = 'Your automation system'
mailTo = ['abc@gmail.com','xyz@wp.pl']
mailSubject = 'Processing finished successfully'
mailBody = '''Hello
This mail is automated
Best regards
Rafal
'''

message ='''From: {}
Subject: {}

{}'''.format(mailFrom,mailSubject,mailBody)

user = 'rafal.kociecki@gmail.com'
password = ''

try:
    server = smtplib.SMTP_SSL('smtp.gmail',465)
    server.ehlo()
    server.login(user,password)
    server.sendmail(user,mailTo,message)
    server.close()
    print('mail sent')
except:
    print('error')

###############################################################################

def SendInfoEmail(user,password,mailFrom,mailTo,mailSubject,mailBody):
    message = '''From: {}
    Subject: {}
    {}'''.format(mailFrom, mailSubject, mailBody)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, mailTo, message)
        server.close()
        print('mail sent')
        return True
    except:
        print('error')
        return False

user = 'rafal.kociecki@gmail.com'
password = ''

SendInfoEmailFromGmail = functools.partial(SendInfoEmail,user,password,mailSubject = 'Execution')

SendInfoEmailFromGmail(mailFrom = mailFrom,mailTo = mailTo,mailBody = mailBody)