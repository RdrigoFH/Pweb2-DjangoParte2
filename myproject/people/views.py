from django.shortcuts import render
from .models import Person

def index(request):
    people = Person.objects.all()  
    return render(request, 'people/index.html', {'people': people})
