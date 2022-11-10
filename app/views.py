from django.shortcuts import render
from app.forms import RegisterForm

# Create your views here.
def drone(request):
    data={}
    data['form']=RegisterForm(request.POST or None)
    if data['form'].is_valid():
        data['form'].save()

    return render(request, 'drone.html', data)