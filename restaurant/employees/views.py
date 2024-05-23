from django.shortcuts import render
from django.http import HttpResponse

from .forms import EmployeeForm

from models import Employee
# Create your views here.

def create_employee(request, ):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
                form.save()
                return HttpResponse('Employee created')
    else:
        return HttpResponse('Method not allowed', status=400)
    ...