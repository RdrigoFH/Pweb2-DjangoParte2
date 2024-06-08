from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Person

def index(request):
    people = Person.objects.all()
    return render(request, 'people/index.html', {'people': people})

class PersonDetailView(DetailView):
    model = Person
    template_name = 'people/person_detail.html'
    context_object_name = 'person'
