# Generated by Django 5.1.3 on 2024-11-18 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
