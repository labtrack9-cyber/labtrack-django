from rest_framework.serializers import ModelSerializer

from labtrackapp.models import *

class LoginTableSerializer(ModelSerializer):
    class Meta:
        model = LoginTable
        fields = ['username','password','usertype']

class LabTableSerializer(ModelSerializer):
    class Meta:
        model = LabTable
        fields = ['labname']

class UserTableSerializer(ModelSerializer):
    class Meta:
        model = UserTable
        fields = ['admissionno','name','program','mobno','dob','gender','bloodgroup','semester','email']

class LabassistantTableSerializer(ModelSerializer):
    class Meta:
        model = LabassistantTable
        fields = ['LOGINID','name','staffid','email','LABID']

class LabmanagerSerializer(ModelSerializer):
    class Meta:
        model = LabmanagerTable
        fields = ['LOGINID','name','staffid','email','LABID']

class InventoryTableSerializer(ModelSerializer):
    class Meta:
        model = InventoryTable
        fields = ['LABMANAGERID','itemname','itemdiscription','quantity']

class ComplaintTableSerializer(ModelSerializer):
    class Meta:
        model = ComplaintTable
        fields = ['user','Complaint','replay']

class FeedbackTableSerializer(ModelSerializer):
    class Meta:
        model = FeedbackTable
        fields = ['user','Feedback']

class TaskTableSerializer(ModelSerializer):
    class Meta:
        model = TaskTable
        fields = ['LABASSISTANTID','USERID','experiment','status']

class LabassignTableSerializer(ModelSerializer):
    class Meta:
        model = LabassignTable
        fields = ['userLABASSISTANTID','lab']

class NotificationTableSerializer(ModelSerializer):
    class Meta:
        model = NotificationTable
        fields = ['USERID','LABASSISTANTID','subject','notificationdetails']

class StudentlabassignTableSerializer(ModelSerializer):
    class Meta:
        model = StudentlabassignTable
        fields = ['USERID','lab']




