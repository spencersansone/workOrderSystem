from django.db import models
from django.contrib.auth.models import User,Group
# from django.contrib.auth.models import Group
import smtplib
from email.mime.text import MIMEText
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class UserProfile(models.Model):
    user_account = models.ForeignKey(User, on_delete=models.CASCADE)
    user_group = models.ForeignKey(Group, on_delete=models.CASCADE).
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


def get_full_name(self):
    try:
        obj = UserProfile.objects.get(user_account=self)
    except:
        return self.username
    first_name = obj.first_name
    last_name = obj.last_name
    return "{} {}".format(first_name,last_name)
    
User.add_to_class("__str__", get_full_name)
    

GMAIL_EMAIL = "chainjourney@gmail.com"
GMAIL_PASSWORD = "Test1234!"

LOCATION_CHOICES = (
    ("B1","Building 1"),
    ("B2","Building 2"),
    ("B3","Building 3"),
    ("B4","Building 4"),
)

def sendGmail(info):
    msg = MIMEText(info['b'])
    msg['Subject'] = info['s']
    msg['From'] = info['g_sender']
    msg['To'] = info['r_email']
    try:
        print("Attempting to send, please wait...")
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(info['g_sender'], info['g_pass'])
        server.sendmail(info['g_sender'], info['r_email'], msg.as_string())
        server.close()
        print('Email sent!')
    except:
        print('Something went wrong...')



class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100,choices=LOCATION_CHOICES)
    room_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class CommonArea(models.Model):
    area_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100,choices=LOCATION_CHOICES)
    
    def __str__(self):
        return "{}:{}".format(self.location,self.area_name)

class ClientRequest(models.Model):
    title = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.TextField(max_length=10000)
    due_date = models.DateField()
    technician = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'groups__name': 'Technicians'})
    notify_technician = models.BooleanField()
    
    def clean(self):
        
        userProfObj = UserProfile.objects.get(user_account=self.technician)
        
        if self.notify_technician:
            if not userProfObj.email:
                raise ValidationError(_('This technician does not have an email listed.'))
            info = {}
            info['g_sender'] = GMAIL_EMAIL
            info['g_pass'] = GMAIL_PASSWORD
            info['r_email'] = userProfObj.email
            info['s'] = "New Work Order: {}".format(self.title)
            info['b'] = """Hello {},

New work order assignment:

    Title: {}
    Description: {}
    Client: {}
    Location: {}
    Room #: {}
    Due Date: {}

Sincerely,
    The Work Order System
""".format(userProfObj.__str__(),
            self.title,
            self.description,
            self.client,
            self.client.location,
            self.client.room_number,
            self.due_date)
            sendGmail(info)
        
class CommonAreaRequest(models.Model):
    title = models.CharField(max_length=100)
    common_area = models.ForeignKey(CommonArea, on_delete=models.CASCADE)
    description = models.TextField(max_length=10000)
    due_date = models.DateField()
    technician = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        limit_choices_to={'groups__name': "Technicians"})
    notify_technician = models.BooleanField()
    
    def clean(self):
        
        userProfObj = UserProfile.objects.get(user_account=self.technician)
        
        if self.notify_technician:
            if not userProfObj.email:
                raise ValidationError(_('This technician does not have an email listed.'))
            info = {}
            info['g_sender'] = GMAIL_EMAIL
            info['g_pass'] = GMAIL_PASSWORD
            info['r_email'] = userProfObj.email
            info['s'] = "New Work Order: {}".format(self.title)
            info['b'] = """Hello {},

New work order assignment:

    Title: {}
    Description: {}
    Common Area: {}
    Location: {}
    Due Date: {}

Sincerely,
    The Work Order System
""".format(userProfObj.__str__(),
            self.title,
            self.description,
            self.common_area.area_nameeman_aera.,
            self.common_area.location,
            self.due_date)
            sendGmail(info)
            

    