from django.shortcuts import render
from django.http import HttpResponse

from .forms import EmployeeForm


def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
                form.save()
                return HttpResponse('Employee created')
    elif request.method == 'GET':
        form = EmployeeForm()
        context = {'form': form}
        return render(request, 'create_employee.html', context)
    else:
        return HttpResponse('Method not allowed', status=400)