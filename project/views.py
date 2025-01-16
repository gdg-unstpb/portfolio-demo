from django.shortcuts import render

# Create your views here.
from .models import Project
def home_page(request):
    projects = Project.objects.all()
    return render(request,'project/home.html',{'projects':projects})


def project_detail(request,id):
    project = Project.objects.get(id=id)
    return render(request,'project/project_detail.html',{'project':project})