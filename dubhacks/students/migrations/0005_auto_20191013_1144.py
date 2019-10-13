# Generated by Django 2.0.3 on 2019-10-13 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='answer',
            name='gpa',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
    ]
