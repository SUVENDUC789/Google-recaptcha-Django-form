# Generated by Django 4.1 on 2022-11-25 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('email', models.CharField(max_length=1150)),
                ('phone', models.CharField(max_length=100)),
                ('aboutcourse', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
