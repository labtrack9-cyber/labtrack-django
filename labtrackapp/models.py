from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    usertype=models.CharField(max_length=100,null=True,blank=True)

class LabTable(models.Model):
    labname=models.CharField(max_length=50,null=True,blank=True)
    
class UserTable(models.Model):
    admissionno=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    program=models.CharField(max_length=100,null=True,blank=True)
    mobno=models.BigIntegerField(null=True,blank=True)
    dob=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,blank=True)
    bloodgroup=models.CharField(max_length=20,null=True,blank=True)
    semester=models.CharField(max_length=20,null=True,blank=True)
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    Class=models.CharField(max_length=100,null=True,blank=True)
class LabassistantTable(models.Model):
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=25,null=True,blank=True)
    staffid=models.IntegerField(null=True,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    LABID=models.ForeignKey(LabTable,on_delete=models.CASCADE,null=True,blank=True)
   
class LabmanagerTable(models.Model):
     LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
     name=models.CharField(max_length=25,null=True,blank=True)
     staffid=models.IntegerField(null=True,blank=True)
    #  department=models.CharField(max_length=25,null=True,blank=True)
     email=models.CharField(max_length=50,null=True,blank=True)
     LABID=models.ForeignKey(LabTable,on_delete=models.CASCADE,null=True,blank=True)
class InventoryTable(models.Model):
    LABMANAGERID=models.ForeignKey(LabmanagerTable,on_delete=models.CASCADE,null=True,blank=True)
    itemname=models.CharField(max_length=50,null=True,blank=True)
    itemdiscription=models.CharField(max_length=100,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
class ComplaintTable(models.Model):
    user=models.ForeignKey(UserTable,on_delete=models.CASCADE,null=True,blank=True)
    Complaint=models.CharField(max_length=100,null=True,blank=True)
    replay=models.CharField(max_length=100,null=True,blank=True)
class FeedbackTable(models.Model):
    user=models.ForeignKey(UserTable,on_delete=models.CASCADE,null=True,blank=True)
    Feedback=models.CharField(max_length=100,null=True,blank=True)
class TaskTable(models.Model):
    LABASSISTENTID=models.ForeignKey(LabassistantTable,on_delete=models.CASCADE,null=True,blank=True)
    USERID=models.ForeignKey(UserTable,on_delete=models.CASCADE,null=True,blank=True)
    experiment=models.CharField(max_length=100,null=True,blank=True)
    status=models.CharField(max_length=100,null=True,blank=True)
    date=models.DateField(null=True,blank=True, auto_now_add=True)
    duedate=models.DateField(null=True,blank=True)

class LabassignTable(models.Model):
    LABASSISTENTID=models.ForeignKey(LabassistantTable,on_delete=models.CASCADE,null=True,blank=True)
    LABID=models.ForeignKey(LabTable,on_delete=models.CASCADE,null=True,blank=True)
class NotificationTable(models.Model):
    USERID=models.ForeignKey(UserTable,on_delete=models.CASCADE,null=True,blank=True)
    LABASSISTENTID=models.ForeignKey(LabassistantTable,on_delete=models.CASCADE,null=True,blank=True)
    subject=models.CharField(max_length=100,null=True,blank=True)
    notificationdetails=models.CharField(max_length=100,null=True,blank=True)
class StudentlabassignTable(models.Model):
    USERID=models.ForeignKey(UserTable,on_delete=models.CASCADE,null=True,blank=True)
    LABID=models.ForeignKey(LabTable,on_delete=models.CASCADE,null=True,blank=True)
    time=models.DateTimeField(null=True,blank=True)



