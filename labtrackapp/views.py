from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from labtrackapp.forms import *
from labtrackapp.models import *

# Create your views here.

class Loginpage(View):
    def get(self, request):
        return render(request, 'loginpage.html')
    def post(self,request):
        Username1=request.POST['Username']
        Password1=request.POST['Password']
        try:
            login_obj=LoginTable.objects.get(username=Username1,password=Password1)
            request.session['userid']=login_obj.id
            print(request.session['userid'])

            if login_obj.usertype=="admin":
                return HttpResponse('''<script>alert("admin_home");window.location=("/Homepage")</script>''')
            elif login_obj.usertype=="labmanager":
                return HttpResponse('''<script>alert("labmanager_home");window.location=("/Homepage_hsptl")</script>''')
            else:
                return HttpResponse('''<script>("invalid user");window.location=("/")</script>''')
        except LoginTable.DoesNotExist:
            return HttpResponse('''<script>alert("invalid username or password"); window.location='/'</script>''')
        



class Homepage(View):
    def get(self, request):
        return render(request,'adminpanel/homepage.html')
class Assignlab(View):
    def get(self, request):
        return render(request,'adminpanel/assign.labs.html')
    
class Labassistant(View):
    def get(self, request):
        c = LabassistantTable.objects.all()
        return render(request,'adminpanel/lab_assistant.html',{'assistant':c})
    
class Labmanager(View):
    def get(self, requst):
        c = LabmanagerTable.objects.all()
        return render(requst,'adminpanel/lab_manager.html',{'manager':c})
    
class Inventory(View):
    def get(self, requst):
        c = InventoryTable.objects.all()
        return render(requst,'adminpanel/inventory.html',{'inventory':c})
    
class Complaints(View):
    def get(self, requst):
        c = ComplaintTable.objects.all()
        return render(requst,'adminpanel/complaints.html',{'complaints':c})
    
class ComplaintReply(View):
    def post(self,request,id):
        c = ComplaintTable.objects.get(id=id)
        d = ReplyForm(request.POST, instance=c)
        if d.is_valid():
            d.save()
            return redirect('/Complaints')
    
class Feedback(View):
    def get(self, requst):
        c = FeedbackTable.objects.all()
        return render(requst,'adminpanel/feedback.html',{'feedback':c})
    
class Addassistant(View):
    def get(self, requst):
        c=LabTable.objects.all()
        print('****************')
        print(c)
        print('****************')
        return render(requst,'adminpanel/addassistant.html',{'lab':c})
    def post(self,request):
        form=AssistantForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.LOGINID=LoginTable.objects.create(username=f.email,password=request.POST['password'],usertype='labassistant')
            f.save()
            return HttpResponse('''<script>alert("Registered Successfully");window.location=("/Labassistant")</script>''')
        
class Editassistant(View):
    def get(self, request, id):
        obj = LabassistantTable.objects.get(id=id)
        labs = LabTable.objects.all()
        return render(request, 'adminpanel/editassistant.html', {
            'edit': obj,
            'lab': labs})
    def post(self, request, id):
        obj = LabassistantTable.objects.get(id=id)

        obj.name = request.POST.get('name')
        obj.staffid = request.POST.get('staffid')
        obj.email = request.POST.get('email')

        lab_id = request.POST.get('LABID')
        if lab_id:
            obj.LABID = LabTable.objects.get(id=lab_id)

        obj.save()

        return HttpResponse('''<script>alert("Updated Successfully");window.location=("/Labassistant")</script>''')


    
    
class Addmanager(View):
    def get(self, requst):
        c=LabTable.objects.all()
        print('****************')
        print(c)
        print('****************')
        return render(requst,'adminpanel/addmanager.html',{'lab':c})
    def post(self,request):
        form=ManagerForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.LOGINID=LoginTable.objects.create(username=f.email,password=request.POST['password'],usertype='labmanager')
            f.save()
            return HttpResponse('''<script>alert("Registered Successfully");window.location=("/Labmanager")</script>''')

class Editmanager(View):
    def get(self, request, id):
        obj = LabmanagerTable.objects.get(id=id)
        labs = LabTable.objects.all()
        return render(request, 'adminpanel/editmanager.html', {
            'edit': obj,
            'lab': labs})
    def post(self, request, id):
        obj = LabmanagerTable.objects.get(id=id)

        obj.name = request.POST.get('name')
        obj.staffid = request.POST.get('staffid')
        obj.email = request.POST.get('email')

        lab_id = request.POST.get('LABID')
        if lab_id:
            obj.LABID = LabTable.objects.get(id=lab_id)

        obj.save()

        return HttpResponse('''<script>alert("Updated Successfully");window.location=("/Labmanager")</script>''')


    
class User(View):
    def get(self, requst):
        c = UserTable.objects.all()
        return render(requst,'adminpanel/viewstudents.html',{'students':c})
    
#######################################################################################

class Addstock(View):
    def get(self, requst):
        return render(requst,'labmanager/addpage.html')
class Editstock(View):
    def get(self, requst):
        return render(requst,'labmanager/editpage.html')   
class Deletestock(View):
    def get(self, requst):
        return render(requst,'labmanager/deletepage.html')
class Viewstock(View):
    def get(self, requst):
        return render(requst,'labmanager/stockpage.html')
class Managerhome(View):
    def get(self, requst):
        return render(requst,'labmanager/managerhome.html')