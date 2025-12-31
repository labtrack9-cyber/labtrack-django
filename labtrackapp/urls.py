
from django.urls import path
from labtrackapp.views import *


urlpatterns = [
    path('', Loginpage.as_view(), name='Loginpage'),
    path('Homepage',Homepage.as_view(), name='Homepage' ),
    path('Assignlab', Assignlab.as_view(), name='Assignlab'),
    path('Labassistant', Labassistant.as_view(), name='Labassistant'),
    path('Labmanager', Labmanager.as_view(), name='Labmanager'),
    path('Inventory', Inventory.as_view(), name='Inventory'),
    path('Complaints', Complaints.as_view(), name='Complaints'),
    path('Feedback', Feedback.as_view(), name='Feedback'),
    path('Addassistant', Addassistant.as_view(), name='Addassistant'),
    path('Editassistant/<int:id>',Editassistant.as_view(), name='Editassistant'),
    path('Deleteassistant/<int:id>',Deleteassistant.as_view(), name='Deleteassistant'),
    path('Addmanager', Addmanager.as_view(), name='Addmanager'),
    path('Editmanager/<int:id>',Editmanager.as_view(), name='Editmanager'),
    path('Deletemanager/<int:id>',Deletemanager.as_view(), name='Deletemanager'),
    path('Viewuser',User.as_view(), name='Viewuser'),
    path('reply/<int:id>', ComplaintReply.as_view()),
#####################################################################################
     path('Addstock', Addstock.as_view(), name='Addstock'),
     path('Editstock/<int:id>', Editstock.as_view(), name='Editstock'),
     path('Deletestock/<int:id>', Deletestock.as_view(), name='Deletestock'),
     path('Viewstock', Viewstock.as_view(), name='Viewstock'),
     path('Managerhome', Managerhome.as_view(), name='Managerhome'),


     ################################################ API #########################################

     path('userreg', UserReg_api.as_view()),
     path('login', LoginAPI.as_view()),
     path('complaint/<int:id>', ComplaintAPI.as_view()),
     path('feedback/<int:id>',FeedbackAPI.as_view()),
     path('assignedlab/<int:id>',AssignedlabAPI.as_view()),
     path('task/<int:id>',ViewTaskAPI.as_view()),
]

