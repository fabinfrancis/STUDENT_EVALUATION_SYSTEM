# Generated by Django 4.1.5 on 2023-04-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0006_students_reg_no_students_semester_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentresult',
            name='seminar',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='studentresult',
            name='t1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='studentresult',
            name='t2',
            field=models.FloatField(default=0),
        ),
    ]
