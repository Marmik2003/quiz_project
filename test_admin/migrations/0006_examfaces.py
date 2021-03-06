# Generated by Django 3.2.6 on 2021-08-21 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_admin', '0005_examresult_forumreply_questionforum_questionresponse'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamFaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face', models.ImageField(upload_to='student_faces/')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_admin.examset')),
            ],
        ),
    ]
