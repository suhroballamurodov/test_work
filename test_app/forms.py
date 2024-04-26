from django import forms
from .models import ClientModel, DeveloperModel

class ClientForms(forms.ModelForm):
    class Meta:

        model = ClientModel
        fields = ('name','contact','project_info','price','create_time','finished_date','status')

class DeveloperForms(forms.ModelForm):
    class Meta:

        model = DeveloperModel
        fields = ('name','contact','my_info','experience_year','finished_work')