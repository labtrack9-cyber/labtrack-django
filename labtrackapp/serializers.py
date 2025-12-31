from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

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
        fields = ['LABASSISTENTID','USERID','experiment','status', 'duedate']

class LabassignTableSerializer(ModelSerializer):
    class Meta:
        model = LabassignTable
        fields = ['userLABASSISTANTID','lab']

class NotificationTableSerializer(ModelSerializer):
    class Meta:
        model = NotificationTable
        fields = ['USERID','LABASSISTANTID','subject','notificationdetails']


from rest_framework import serializers
from .models import StudentlabassignTable, LabassistantTable

class StudentlabassignTableSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='USERID.name', read_only=True)
    lab_name = serializers.CharField(source='LABID.labname', read_only=True)

    labassistant_name = serializers.SerializerMethodField()
    labassistant_email = serializers.SerializerMethodField()
    labassistant_staffid = serializers.SerializerMethodField()

    class Meta:
        model = StudentlabassignTable
        fields = [
            'USERID',
            'LABID',
            'user_name',
            'lab_name',
            'time',
            'labassistant_name',
            'labassistant_email',
            'labassistant_staffid',
        ]

    def get_labassistant_name(self, obj):
        assistant = LabassistantTable.objects.filter(LABID=obj.LABID).first()
        return assistant.name if assistant else None

    def get_labassistant_email(self, obj):
        assistant = LabassistantTable.objects.filter(LABID=obj.LABID).first()
        return assistant.email if assistant else None

    def get_labassistant_staffid(self, obj):
        assistant = LabassistantTable.objects.filter(LABID=obj.LABID).first()
        return assistant.staffid if assistant else None





