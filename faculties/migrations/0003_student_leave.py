# Generated by Django 3.0 on 2020-01-14 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculties', '0002_auto_20200114_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fbatch', models.CharField(max_length=10)),
                ('sname', models.CharField(max_length=100)),
                ('srollno', models.IntegerField()),
                ('sleave_from', models.CharField(max_length=50)),
                ('sleave_to', models.CharField(max_length=50)),
                ('sleave_type', models.CharField(max_length=100)),
                ('sleave_reason', models.CharField(max_length=500)),
                ('sleave_status', models.CharField(default='pending', max_length=50)),
            ],
            options={
                'db_table': 'student-leave',
            },
        ),
    ]
