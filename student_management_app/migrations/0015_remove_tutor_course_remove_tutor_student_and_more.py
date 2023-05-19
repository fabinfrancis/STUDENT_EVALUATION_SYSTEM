# Generated by Django 4.1.5 on 2023-04-02 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0014_remove_tutor_course_id_remove_tutor_student_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='course',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='student',
        ),
        migrations.AddField(
            model_name='tutor',
            name='course_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student_management_app.courses'),
        ),
        migrations.AddField(
            model_name='tutor',
            name='student_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tutor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='tutor_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
