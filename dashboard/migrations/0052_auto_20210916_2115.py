# Generated by Django 3.2.7 on 2021-09-17 01:15

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0051_alter_palaceentry_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='palaceentry',
            name='hyperlink',
            field=models.URLField(blank=True, help_text='An external link of your choice'),
        ),
        migrations.AlterField(
            model_name='palaceentry',
            name='image',
            field=models.ImageField(blank=True, help_text='Optional small photo that will appear next to your entry, no more than 1 megabyte', null=True, upload_to=dashboard.models.achievement_image_file_name, validators=[dashboard.models.validate_at_most_1mb]),
        ),
    ]
