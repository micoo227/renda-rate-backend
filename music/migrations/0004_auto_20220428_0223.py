# Generated by Django 3.2.13 on 2022-04-28 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_rating_artist_alter_rating_song_delete_artist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='username',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
