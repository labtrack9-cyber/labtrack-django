from django.contrib import admin

from labtrackapp.models import *

# Register your models here.
admin.site.register(LoginTable)
admin.site.register(UserTable)
admin.site.register(LabassistantTable)
admin.site.register(LabmanagerTable)
admin.site.register(InventoryTable)
admin.site.register(ComplaintTable)
admin.site.register(FeedbackTable)
admin.site.register(TaskTable)
admin.site.register(LabassignTable)
admin.site.register(NotificationTable)
admin.site.register(StudentlabassignTable)
admin.site.register(LabTable)