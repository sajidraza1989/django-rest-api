from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def employee(request):
    emp = {
        'id': 1,
        'name': 'John Doe',
        'age': 30,
        'department': 'Engineering',
        'salary': 70000
    }
    return JsonResponse(emp)