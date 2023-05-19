# Generated by Django 4.1.5 on 2023-04-07 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "student_management_app",
            "0015_remove_tutor_course_remove_tutor_student_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="user_type",
            field=models.CharField(
                choices=[(1, "HOD"), (2, "Staff"), (3, "Student"), (4, "Tutor")],
                default=1,
                max_length=10,
            ),
        ),
    ]
