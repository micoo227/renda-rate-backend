# Generated by Django 4.0.3 on 2022-03-11 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('song', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('genre', models.CharField(max_length=255)),
                ('album', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('artist', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('birthplace', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.artist')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.user')),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='music.biography'),
        ),
    ]
