# Generated by Django 3.2.6 on 2021-08-20 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_admin', '0003_alter_examset_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='CORRECT_ANS',
            new_name='correct_ans',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_test',
            new_name='question_text',
        ),
        migrations.AddField(
            model_name='question',
            name='pr10',
            field=models.ImageField(blank=True, null=True, upload_to='problems/img/'),
        ),
        migrations.AddField(
            model_name='question',
            name='pr11',
            field=models.ImageField(blank=True, null=True, upload_to='problems/img/'),
        ),
        migrations.AddField(
            model_name='question',
            name='pr12',
            field=models.ImageField(blank=True, null=True, upload_to='problems/img/'),
        ),
        migrations.AddField(
            model_name='question',
            name='pr2',
            field=models.ImageField(blank=True, null=True, upload_to='problems/img/'),
        ),
        migrations.AddField(
            model_name='question',
            name='pr3',
            field=models.ImageField(blank=True, null=True, upload_to='problems/img/'),
        ),
        migrations.AddField(
            model_name='question',
            name='pr4',
            field=models.ImageField(blank=True, null=True, upload_to='problems/img/'),
        ),
        migrations.AddField(
            model_name='question',
            name='pr5',
            field=models.ImageField(blank=True, null=True, upload_to='problems/img/'),
        ),
        migrations.AddField(
            model_name='question',
            name='pr6',
            field=models.ImageField(blank=True, null=True, upload_to='problems/img/'),
        ),
        migrations.AddField(
            model_name='question',
            name='pr7',
            field=models.ImageField(blank=True, null=True, upload_to='problems/img/'),
        ),
        migrations.AddField(
            model_name='question',
            name='pr8',
            field=models.ImageField(blank=True, null=True, upload_to='problems/img/'),
        ),
        migrations.AddField(
            model_name='question',
            name='pr9',
            field=models.ImageField(blank=True, null=True, upload_to='problems/img/'),
        ),
        migrations.AddField(
            model_name='question',
            name='sq',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='sr1',
            field=models.ImageField(blank=True, null=True, upload_to='solutions/img/'),
        ),
        migrations.AddField(
            model_name='question',
            name='sr10',
            field=models.ImageField(blank=True, null=True, upload_to='solutions/img/'),
        ),
        migrations.AddField(
            model_name='question',
            name='sr2',
            field=models.ImageField(blank=True, null=True, upload_to='solutions/img/'),
        ),
        migrations.AddField(
            model_name='question',
            name='sr3',
            field=models.ImageField(blank=True, null=True, upload_to='solutions/img/'),
        ),
        migrations.AddField(
            model_name='question',
            name='sr4',
            field=models.ImageField(blank=True, null=True, upload_to='solutions/img/'),
        ),
        migrations.AddField(
            model_name='question',
            name='sr5',
            field=models.ImageField(blank=True, null=True, upload_to='solutions/img/'),
        ),
        migrations.AddField(
            model_name='question',
            name='sr6',
            field=models.ImageField(blank=True, null=True, upload_to='solutions/img/'),
        ),
        migrations.AddField(
            model_name='question',
            name='sr7',
            field=models.ImageField(blank=True, null=True, upload_to='solutions/img/'),
        ),
        migrations.AddField(
            model_name='question',
            name='sr8',
            field=models.ImageField(blank=True, null=True, upload_to='solutions/img/'),
        ),
        migrations.AddField(
            model_name='question',
            name='sr9',
            field=models.ImageField(blank=True, null=True, upload_to='solutions/img/'),
        ),
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='test_admin.subject'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='subject_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='test_admin.subjecttype'),
            preserve_default=False,
        ),
    ]
