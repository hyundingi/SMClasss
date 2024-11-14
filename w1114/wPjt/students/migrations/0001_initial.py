# Generated by Django 5.1.3 on 2024-11-14 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=100)),
                ('s_major', models.CharField(max_length=100)),
                ('s_age', models.IntegerField(default=0)),
            ],
        ),
    ]
