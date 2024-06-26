# Generated by Django 5.0.4 on 2024-04-26 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('contact', models.CharField(max_length=15, verbose_name='Phone')),
                ('project_info', models.TextField(verbose_name='Project infos')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('create_time', models.DateTimeField(verbose_name='Created date')),
                ('finished_date', models.DateTimeField(verbose_name='Finished date')),
                ('status', models.CharField(choices=[('active', 'Aktiv'), ('noactive', 'Noaktive')], default='active', max_length=8, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='DeveloperModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('contact', models.CharField(max_length=15, verbose_name='Phone')),
                ('my_info', models.TextField(verbose_name='About me')),
                ('experience_year', models.IntegerField(verbose_name='Experience year')),
                ('finished_work', models.IntegerField(verbose_name='Completed projects')),
            ],
            options={
                'verbose_name': 'Developer',
                'verbose_name_plural': 'Developers',
            },
        ),
    ]
