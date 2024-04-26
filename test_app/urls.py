from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('', home, name = 'home'),
    path('kworksayt',kworksayt, name='kworksayt'),
    
    path('project/', ProjectListView.as_view(), name='project'),
    path('create_project', ProjectCreateView.as_view(), name='create_project'),
    path('project_view/<str:pk>', ProjectDetailView.as_view(), name='project_view'),
    path('project_delete/<str:pk>',ProjectDeleteView.as_view(), name='project_delete'),
    path('project_update/<str:pk>', ProjectUpdateView.as_view(), name='project_update'),

    path('developer/', DeveloperListView.as_view(), name='developer'),
    path('create_developer', DeveloperCreateView.as_view(), name='create_developer'),
    path('developer_view/<str:pk>', DeveloperDetailView.as_view(), name='developer_view'),
    path('developer_delete/<str:pk>',DeveloperDeleteView.as_view(), name='developer_delete'),
    path('developer_update/<str:pk>', DeveloperUpdateView.as_view(), name='developer_update'),
]