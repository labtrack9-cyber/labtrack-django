from django.forms import ModelForm

from labtrackapp.models import *


class ReplyForm(ModelForm):
    class Meta:
        model=ComplaintTable
        fields=['replay']
class AssistantForm(ModelForm):
    class Meta:
        model=LabassistantTable
        fields='__all__'
class ManagerForm(ModelForm):
    class Meta:
        model=LabmanagerTable
        fields='__all__'
        
class InventoryForm(ModelForm):
    class Meta:
        model=InventoryTable
        fields='__all__'