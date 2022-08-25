# Generated by Django 4.0.6 on 2022-08-25 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('debut', models.DateTimeField()),
                ('country', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
