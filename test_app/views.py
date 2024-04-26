from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from .models import ClientModel, DeveloperModel
from .forms import ClientForms, DeveloperForms
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


#clients_project
class ProjectListView(ListView):
    model = ClientModel
    template_name = 'projects.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        projects = ClientModel.objects.all()
        context ['projects'] = projects
        return context


class ProjectDetailView(DetailView):
    model = ClientModel
    template_name = 'view.html'
    context_object_name = 'project'


class ProjectCreateView(CreateView):
    model = ClientModel
    template_name = 'create.html'
    fields = ('name','contact','project_info','price','create_time','finished_date','status')
    success_url = reverse_lazy('project')


# def productCreate(request):  
#     if request.method == "POST":  
#         form = ProductForm(request.POST)  
#         if form.is_valid():   
#             form.save() 
#             model = form.instance
#             return redirect('projects')  
#     else:  
#         form = ProductForm()  
#     return render(request,'create.html',{'form':form})  


class ProjectUpdateView(UpdateView):
    model = ClientModel
    fields = ('name','contact','project_info','price','create_time','finished_date','status')
    template_name = 'update.html'
    success_url = reverse_lazy('project')


class ProjectDeleteView(DeleteView):
    model = ClientModel
    template_name = 'delete.html'
    success_url = reverse_lazy('project')



#developer

class DeveloperListView(ListView):
    model = DeveloperModel
    template_name = 'developers.html'
    context_object_name = 'developers'

    def get_context_data(self, **kwargs):
        context = super(DeveloperListView, self).get_context_data(**kwargs)
        developers = DeveloperModel.objects.all()
        context ['developers'] = developers
        return context


class DeveloperDetailView(DetailView):
    model = DeveloperModel
    template_name = 'view_developer.html'
    context_object_name = 'developer'
    success_url = reverse_lazy('developer')

    


class DeveloperCreateView(CreateView):
    model = DeveloperModel
    template_name = 'create_developer.html'
    fields = ('name','contact','my_info','experience_year','finished_work')
    success_url = reverse_lazy('developer')


# def productCreate(request):  
#     if request.method == "POST":  
#         form = ProductForm(request.POST)  
#         if form.is_valid():   
#             form.save() 
#             model = form.instance
#             return redirect('developer')  
#     else:  
#         form = ProductForm()  
#     return render(request,'create.html',{'form':form})  


class DeveloperUpdateView(UpdateView):
    model = DeveloperModel
    fields = ('name','contact','my_info','experience_year','finished_work')
    template_name = 'update_developer.html'
    success_url = reverse_lazy('developer')


class DeveloperDeleteView(DeleteView):
    model = DeveloperModel
    template_name = 'delete_developer.html'
    success_url = reverse_lazy('developer')


def kworksayt(request):
    return render(request, template_name='kworksayt.html',context={})

def home(request):
    return render(request,'home.html')


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"