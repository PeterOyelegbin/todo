from django.views import generic
from .models import Todo
from .form import TodoForm

# Create your views here.
class HomePage(generic.ListView):
    queryset = Todo.objects.all()
    template_name = "home.html"

# About page
class AboutPage(generic.TemplateView):
    template_name = "about.html"

# Add task
class AddItem(generic.CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'add.html'
    success_url = '/'

# Task details
class DetailItem(generic.DetailView):
    queryset = Todo.objects.all()
    template_name = 'details.html'

# Update task
class UpdateItem(generic.UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'update.html'
    success_url = '/'

# Delete task
class DeleteItem(generic.DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = '/'
