# Generated by Django 3.2.5 on 2021-07-27 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0056_auto_20210727_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='parent_email',
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='first_name',
            field=models.CharField(help_text='Your first name', max_length=128),
        ),
    ]
