# Generated by Django 3.1.2 on 2020-10-23 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenreTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_name', models.CharField(max_length=40)),
                ('short_name', models.CharField(blank=True, max_length=40, null=True)),
                ('show_name', models.BooleanField(blank=True, default=True, null=True)),
                ('is_important', models.BooleanField(blank=True, default=True, null=True)),
                ('icon', models.CharField(blank=True, max_length=50, null=True)),
                ('show_icon', models.BooleanField(default=False)),
                ('tag_category', models.CharField(default='genre', max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='genre_tags',
            field=models.ManyToManyField(blank=True, to='games.GenreTag'),
        ),
    ]