# Generated by Django 4.0.6 on 2022-08-25 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_director_alter_artist_name_alter_genre_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='name',
        ),
        migrations.AddField(
            model_name='genre',
            name='title',
            field=models.TextField(null=True),
        ),
    ]