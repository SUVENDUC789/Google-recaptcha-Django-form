# Generated by Django 4.1 on 2022-11-27 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=130)),
                ('lname', models.CharField(max_length=130)),
                ('email', models.CharField(max_length=1300)),
                ('phone', models.CharField(max_length=130)),
                ('grade', models.CharField(max_length=110)),
                ('GuardiansName', models.CharField(max_length=300)),
            ],
        ),
    ]
