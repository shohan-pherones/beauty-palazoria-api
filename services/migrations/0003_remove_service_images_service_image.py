# Generated by Django 5.1.3 on 2024-11-18 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='images',
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
