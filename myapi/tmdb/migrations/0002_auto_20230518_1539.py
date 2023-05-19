# Generated by Django 3.2.18 on 2023-05-18 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tmdb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genres',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='like_users',
        ),
        migrations.DeleteModel(
            name='Actor',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
