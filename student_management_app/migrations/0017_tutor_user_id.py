# Generated by Django 4.1.5 on 2023-04-07 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student_management_app", "0016_alter_customuser_user_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="tutor",
            name="user_id",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]