# Generated by Django 2.0.3 on 2019-10-13 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='notes',
            field=models.CharField(default='', max_length=128),
        ),
    ]
