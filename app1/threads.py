import threading
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import send_mail, EmailMessage

import time

from django.http import HttpResponse


class send_mail_via_thread(threading.Thread):
    def __init__(self , email ):
        self.email = email
        threading.Thread.__init__(self)




    def run(self):

        try:
            subject = 'plz check the students_data'
            message = f'Hi dear, i have sent the user_data,in excel file and in pdf format'
            email_from = settings.EMAIL_HOST_USER

            print('SEND EMAIL STARTED')
            # send_mail(subject , message ,email_from ,[self.email])
            mail = EmailMessage(subject, message, email_from, [self.email])
            # mail.attach("excel_files/student_data.xlsx")
            # mail.attach("app1/pdf/student_info.pdf" )
            mail.attach_file("excel_files/student_data.xlsx")
            mail.attach_file("app1/pdf/student_info.pdf")

            mail.send()
            print('EMAIL SENT')

        except Exception as e:
            print(e)

