from django.http import HttpResponse
from django.shortcuts import render
from . models import *
import pandas,pdfkit,random
import faker
from faker import Faker
fake = Faker()
from .threads import *
# Create your views here.
def fake_generate_data(request):
    for i in range(0,20):

        branches =["computer_science","mechanical","electronics","civil","psychology","architecture"]

        random_list_index = random.randint(1, len(branches))
        print(random_list_index)

        student_obj =StudentModel.objects.create(

            name= fake.name(),

            age = random.randint(18, 54),

            skill= branches[random_list_index-1]
        )
        student_obj.save()
        print('Student created')
    students = StudentModel.objects.all()
    return render(request,"app1/student_info.html",{"students":students})




def excel_file_creation(request):
    data=[]

    student_info = StudentModel.objects.all()
    for student in student_info:
        li =[student.name,student.age,student.address,student.skill]
        data.append(li)
        # print(li)
    # print(data)
    data =pandas.DataFrame(data)
    print(data)
    data.to_excel("excel_files/student_data.xlsx")
    print("done")
    data.to_html("excel_files/student_data.html")
    pdfkit.from_file("excel_files/student_data.html", "app1/pdf/student_info.pdf")
    return HttpResponse("ur excel file got created")


def send_mail_with_attachment(request):
     email_holders = EmailModel.objects.all()
     for email in email_holders:
         send_mail_via_thread(email.email).start()
     return HttpResponse("ur email got sent")


