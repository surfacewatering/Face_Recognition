# Generated by Django 4.0.4 on 2022-05-18 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='face',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pface', models.CharField(max_length=40)),
                ('dt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('rating', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('profession', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='')),
                ('login', models.DateTimeField(auto_now=True)),
                ('attendance', models.BooleanField(default=False)),
                ('phone', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
