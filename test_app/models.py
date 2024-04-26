from django.db import models



# Create your models here.

class ClientModel(models.Model):
    STATUS_CHOICES = (
        ('active', 'Aktiv'),
        ('noactive', 'Noaktive'),
        )
    name = models.CharField(max_length=30,blank=False, verbose_name='Name')
    contact = models.CharField(max_length=15, blank=False, verbose_name='Phone')
    project_info = models.TextField(verbose_name='Project infos')
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=False, verbose_name='Price')
    create_time = models.DateTimeField(auto_now_add=False, verbose_name='Created date')
    finished_date = models.DateTimeField(verbose_name='Finished date')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='active', verbose_name='Status')


    def __str__(self):
        return f'Name: {self.name}, Created: {self.create_time}. Finish: {self.finished_date}'
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

class DeveloperModel(models.Model):
    name = models.CharField(max_length=30,blank=False, verbose_name='Name')
    contact = models.CharField(max_length=15, blank=False, verbose_name='Phone')
    my_info = models.TextField(verbose_name='About me')
    experience_year = models.IntegerField(verbose_name='Experience year')
    finished_work = models.IntegerField(verbose_name='Completed projects')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Developer'
        verbose_name_plural = 'Developers'