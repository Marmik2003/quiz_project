# Generated by Django 3.2.6 on 2021-08-23 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_admin', '0008_questionresponse_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionresponse',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='test_admin.question'),
            preserve_default=False,
        ),
    ]
