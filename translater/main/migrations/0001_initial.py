# Generated by Django 3.1.7 on 2021-04-05 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(max_length=150, unique=True)),
                ('translated_word', models.TextField(max_length=150)),
            ],
        ),
    ]
