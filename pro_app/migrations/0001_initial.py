# Generated by Django 4.1.3 on 2023-03-30 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_list', models.CharField(max_length=250)),
                ('about_text', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
    ]